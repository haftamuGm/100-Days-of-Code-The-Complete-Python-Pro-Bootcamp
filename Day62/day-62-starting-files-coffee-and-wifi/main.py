from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, SubmitField,SelectField,URLField,validators
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location=URLField('Cafe Location on Google Maps (URL)',validators=[validators.DataRequired(),validators.URL(message="Invalid URl")])
    opening_time=StringField('Opening Time e.g 8 AM',validators=[DataRequired()])
    closing_time=StringField('Closing Time e.g 5:30 PM',validators=[DataRequired()])
    coffee_rating=SelectField('Coffee Rating',choices=[
                                                       ("☕"),
                                                       ("☕☕"),
                                                       ("☕☕☕"),
                                                       ("☕☕☕☕"),
                                                       ("☕☕☕☕☕")],
                              validators=[DataRequired()])
    wife_strength_rating=SelectField('Wifi Strength Rating',choices=[
        ("✘"),
        ("💪"),
        ("💪💪"),
        ("💪💪💪"),
        ("💪💪💪💪"),
        ("💪💪💪💪💪")

    ],validators=[DataRequired()])
    power_strength_rating=SelectField('Power Socket Strength Rating',choices=[
        ("✘"),
        ("🔌"),
        ("🔌🔌"),
        ("🔌🔌🔌"),
        ("🔌🔌🔌🔌"),
        ("🔌🔌🔌🔌🔌")

    ],validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["post","get"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv',mode='a',encoding="utf-8") as add_file:
            add_file.write("\n")
            add_file.write(f"{form.cafe_name.data} ,")
            add_file.write(f"{form.cafe_location.data} ,")
            add_file.write(f"{form.opening_time.data} ,")
            add_file.write(f"{form.closing_time.data} ,")
            add_file.write(f"{form.coffee_rating.data} ,")
            add_file.write(f"{form.wife_strength_rating.data} ,")
            add_file.write(f"{form.power_strength_rating.data}")


    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
