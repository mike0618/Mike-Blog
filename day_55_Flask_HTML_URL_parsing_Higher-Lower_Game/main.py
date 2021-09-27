from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


@app.route('/')  # decorator
@app.route('/home')  # different routes
def hello_world():
    # Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif" width=300 alt="Cat picture">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye'


# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == '__main__':
    app.run(debug=True)  # Debug mode to auto-reload
