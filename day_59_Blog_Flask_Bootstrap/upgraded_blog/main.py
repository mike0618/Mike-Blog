from flask import Flask, render_template
from datetime import date
import requests

blog_url = 'https://api.npoint.io/4ac9c32a945d3983ac66'
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()

app = Flask(__name__)


@app.route('/')
def home():
    year = date.today().year
    return render_template("index.html", year=year, posts=all_posts)


@app.route('/about.html')
def about():
    year = date.today().year
    return render_template('about.html', year=year)


@app.route('/contact.html')
def contact():
    year = date.today().year
    return render_template('contact.html', year=year)


@app.route('/post/<int:p_id>')
def get_post(p_id):
    post = all_posts[p_id - 1]
    return render_template('post.html', post=post, image=post['image'])


if __name__ == "__main__":
    app.run(debug=True)
