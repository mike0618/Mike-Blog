from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yYzU8-S*MUba321'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opn = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    cls = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=['☕' * n for n in range(1, 6)], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=['✘'] + ['💪' * n for n in range(1, 6)],
                       validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=['✘'] + ['🔌' * n for n in range(1, 6)],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow((form.cafe.data,
                                 form.location.data,
                                 form.opn.data,
                                 form.cls.data,
                                 form.coffee.data,
                                 form.wifi.data,
                                 form.power.data))
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
