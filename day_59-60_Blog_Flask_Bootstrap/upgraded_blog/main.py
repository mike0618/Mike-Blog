from flask import Flask, render_template, request
from datetime import date
import requests
import smtplib
from my_conf import EMAIL, PASS

blog_url = 'https://api.npoint.io/4ac9c32a945d3983ac66'
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    year = date.today().year
    return render_template("index.html", year=year, posts=all_posts)


@app.route('/about')
def about():
    year = date.today().year
    return render_template('about.html', year=year)


@app.route('/contact', methods=['post', 'get'])
def contact():
    year = date.today().year
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        with smtplib.SMTP('smtp.mail.yahoo.com') as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASS)
            conn.sendmail(from_addr=EMAIL,
                          to_addrs=EMAIL,
                          msg=f'Subject: Message from website.\n\nName: {name}\nEmail: {email}\n'
                              f'Phone: {phone}\nMessage: {message}')
        return render_template('contact.html', year=year, sent=True)
    return render_template('contact.html', year=year, sent=False)


@app.route('/post/<int:p_id>')
def get_post(p_id):
    post = all_posts[p_id - 1]
    return render_template('post.html', post=post, image=post['image'])


if __name__ == "__main__":
    app.run(debug=True)
