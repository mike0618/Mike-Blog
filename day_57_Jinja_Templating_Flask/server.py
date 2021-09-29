from flask import Flask, render_template
from random import randint
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = randint(5, 21)
    current_year = date.today().year
    return render_template('index.html', num=random_num, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    agify = f'https://api.agify.io?name={name}&country_id=US'
    age_resp = requests.get(agify)
    age_resp.raise_for_status()
    age = age_resp.json().get('age')

    genderize = f'https://api.genderize.io?name={name}&country_id=US'
    gen_resp = requests.get(genderize)
    gen_resp.raise_for_status()
    gender = gen_resp.json().get('gender')

    return render_template('guess_name.html', name=name.title(), age=age, gender=gender)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/93885110f9d23d9f41af'
    blog_resp = requests.get(blog_url)
    all_posts = blog_resp.json()
    return render_template('blog.html', posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)