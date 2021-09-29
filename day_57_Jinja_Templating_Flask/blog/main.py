from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/93885110f9d23d9f41af'
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:p_id>')
def get_post(p_id):
    post = all_posts[p_id-1]
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
