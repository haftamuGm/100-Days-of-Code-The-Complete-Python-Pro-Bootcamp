from flask import Flask, render_template,request
import requests
from smtplib import SMTP_SSL

from pyexpat.errors import messages

password="sdypcybuxcvudqii"
own_email="bsrathabtamu4@gmail.com"
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
@app.route("/form-entry", methods=["post"])
def receive_data():
    user_name=request.form["name"]
    my_email=request.form["email"]
    phone_number=request.form["phone"]
    message_=request.form["message"]
    sent(user_name,my_email,phone_number,message_)
    return '<h1>Successfully sent your message</h1>'
def sent(name,email,phone,message):

    with SMTP_SSL("smtp.gmail.com") as con:
        con.login(user=own_email,password=password)
        con.sendmail(from_addr=email,
                     to_addrs="habtamugm16@gmail.com",
                     msg=f"subject:\n\n Name:   {name}\nEmail:   {email}\n Phone number:  {phone}\nMessage:      {message}")
if __name__ == "__main__":
    app.run(debug=True, port=5001)
