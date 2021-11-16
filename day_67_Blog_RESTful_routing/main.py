from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import bleach
# import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Vm433?+EMd%x0'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


## strips invalid tags/attributes
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']

    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }

    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)

    return cleaned


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, year=date.today().year)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post, year=date.today().year)


@app.route("/about")
def about():
    return render_template("about.html", year=date.today().year)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=date.today().year)


@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        body = strip_invalid_html(form.body.data)
        post = BlogPost(title=form.title.data,
                        subtitle=form.subtitle.data,
                        author=form.author.data,
                        img_url=form.img_url.data,
                        body=body,
                        date=date.today().strftime("%B %d, %Y"))
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, year=date.today().year)


@app.route("/post/edit/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(title=post.title,
                          subtitle=post.subtitle,
                          img_url=post.img_url,
                          author=post.author,
                          body=post.body)
    if form.validate_on_submit():
        body = strip_invalid_html(form.body.data)
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.author = form.author.data
        post.body = body
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('make-post.html', form=form, year=date.today().year, edit=True)


@app.route("/post/delete/<int:post_id>")
def delete(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    # webbrowser.open('http://localhost:5000')
    app.run(host='0.0.0.0', port=5000, debug=True)
