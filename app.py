from flask import abort, Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, MessageForm
from flask_gravatar import Gravatar
from bleach import clean
from functools import wraps
import smtplib
from my_conf_google import EMAIL, SMTP_HOST
from email.message import EmailMessage
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)


# Year for all templates
@app.context_processor
def inject_today():
    return {'today': date.today()}


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Connect to LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Gravatar
gravatar = Gravatar(app,
                    size=80,
                    rating='g',
                    default='identicon',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    posts = relationship('BlogPost', back_populates='author')
    comments = relationship('Comment', back_populates='author')


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = relationship('User', back_populates='posts')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship('Comment', back_populates='post')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = relationship('User', back_populates='comments')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post = relationship('BlogPost', back_populates='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))


db.create_all()


# Strip invalid/dangerous tags/attributes
def clean_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike', 'strong',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
    allowed_attrs = {'a': ['href', 'target', 'title'], 'img': ['src', 'alt', 'width', 'height']}
    cleaned = clean(content, tags=allowed_tags, attributes=allowed_attrs, strip=True)
    return cleaned


# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Protect routes
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        return abort(403)

    return decorated_function


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if User.query.filter_by(email=email).first():
            flash("You've already signed up with that email, log in instead.")
            return redirect(url_for('login', email=email))
        user_hash = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=16)
        new_user = User(name=form.name.data,
                        email=email,
                        password=user_hash)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = request.args.get('email')
    if email:
        form.email.data = email
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('That email does not exist, please try again.', 'error')
            return redirect(url_for('login'))
        if not check_password_hash(user.password, form.password.data):
            flash('Invalid password provided', 'error')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Log in or register to comment')
            return redirect(url_for('login'))
        new_comment = Comment(text=clean_html(form.text.data),
                              author=current_user,
                              post=requested_post)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=requested_post.id))
    return render_template("post.html", post=requested_post, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = MessageForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Log in or register to send a message.')
            return redirect(url_for('login'))
        msg = EmailMessage()
        msg['Subject'] = "Message from Mike's Blog."
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg.add_alternative(f"<p><b>Name: {current_user.name}</b></p><p><b>Email: {current_user.email}</b></p>" +
                            clean_html(form.text.data), subtype='html')
        with smtplib.SMTP(SMTP_HOST, port=587) as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=os.environ.get('PASS'))
            conn.send_message(msg)
        flash('Your message was successfully sent.')
        return redirect(url_for('contact'))
    return render_template("contact.html", form=form)


@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(title=form.title.data,
                            subtitle=form.subtitle.data,
                            body=clean_html(form.body.data),
                            img_url=form.img_url.data,
                            author=current_user,
                            date=date.today().strftime("%B %d, %Y"))
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(title=post.title,
                               subtitle=post.subtitle,
                               img_url=post.img_url,
                               body=post.body)
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = clean_html(edit_form.body.data)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
