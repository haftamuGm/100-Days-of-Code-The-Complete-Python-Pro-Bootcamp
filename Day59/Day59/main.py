from flask import Flask,render_template
import requests
import datetime
URL="https://api.npoint.io/674f5423f73deab1e9a7"
all_post=requests.get(URL).json()
y=datetime.datetime.today().year
m=datetime.datetime.today().month
d=datetime.datetime.today().day
app=Flask(__name__)
@app.route("/")

def home():
    return render_template('index.html', allpost=all_post, year=y, month=m, day=d)
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/post/<int:index>")
def post(index):
    result=None
    for post in all_post:
        if  post["id"]==index:
            result=post
    return render_template('post.html',allpost=result, year=y, month=m, day=d)
if __name__ == '__main__':
    app.run(debug=True)

