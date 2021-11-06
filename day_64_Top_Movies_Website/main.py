from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests
from my_conf import API_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yYzU8-S*MUba321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(200), nullable=True)
    img_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title!r}>"


db.create_all()


class MovieEdit(FlaskForm):
    rating = DecimalField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class MovieAdd(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    length = len(all_movies)
    for i in range(length):
        all_movies[i].ranking = length - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/update', methods=['GET', 'POST'])
def update():
    movie_id = request.args.get('m_id')
    movie = Movie.query.get(movie_id)
    form = MovieEdit()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('m_id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = MovieAdd()
    if form.validate_on_submit():
        title = form.title.data
        prm = {'api_key': API_KEY,
               'query': title}
        resp = requests.get('https://api.themoviedb.org/3/search/movie', params=prm)
        resp.raise_for_status()
        entries = resp.json()['results']
        print(entries)
        return render_template('select.html', entries=entries)
    return render_template('add.html', form=form)


@app.route('/found')
def found():
    api_id = request.args.get('api_id')
    if api_id:
        prm = {'api_key': API_KEY}
        resp = requests.get(f'https://api.themoviedb.org/3/movie/{api_id}', params=prm)
        resp.raise_for_status()
        data = resp.json()
        new_movie = Movie()
        new_movie.title = data['title']
        new_movie.year = data['release_date'][:4]
        new_movie.description = data['overview']
        new_movie.img_url = f'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/{data["poster_path"]}'
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('update', m_id=new_movie.id))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
