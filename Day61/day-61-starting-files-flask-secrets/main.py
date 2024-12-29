from ensurepip import bootstrap

from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField
from flask_bootstrap import Bootstrap5
from wtforms import StringField,PasswordField,SubmitField,validators,EmailField
from wtforms.validators import DataRequired,Length,Email
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.DataRequired(), validators.Email()])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=7)])
    submit=SubmitField(label='Login')
app = Flask(__name__)
boot_strap=Bootstrap5(app)
app.secret_key = "some secret string"
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login",methods=["POST","GET"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
