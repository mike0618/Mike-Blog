from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


class MyForm(FlaskForm):
    email = StringField(label='Name', validators=[DataRequired(), Email(), Length(min=6)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')


app = create_app()
app.secret_key = 'yYzU8-S*MUba321'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
