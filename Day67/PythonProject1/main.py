from Tools.scripts.generate_token import token_inc_template
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor=CKEditor(app)

class my_new_post(FlaskForm):
    title=StringField('Blog Post Title',validators=[DataRequired()])
    subtitle=StringField('Subtitle',validators=[DataRequired()])
    author=StringField('Your Name',validators=[DataRequired()])
    img_url=StringField('Blog Image URL',validators=[DataRequired()])
    body=CKEditorField('Content',validators=[DataRequired()])
    submit=SubmitField('Submit Post',validators=[DataRequired()])

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html",all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    print(requested_post.img_url)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post")
def new_post():
    form=my_new_post()
    header="New Post"
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect('home')



    return render_template("make-post.html",form=form,head=header)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>',methods=["GEt","POST"])
def edit_post(post_id):
    header="Edit Post"
    fill=db.get_or_404(BlogPost,post_id)
    form=my_new_post(
        title=fill.title,
        subtitle=fill.subtitle,
        body=fill.body,
        author=fill.author,
        img_url=fill.img_url
    )
    if form.validate_on_submit():

        fill.title=form.title.data
        fill.subtitle=form.subtitle.data
        fill.body=form.body.data
        fill.author=form.author.data
        fill.img_url=form.author.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))



    return render_template("make-post.html",form=form,head=header)
# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<id>")
def delete(id):
    delete_blog=db.get_or_404(BlogPost,id)
    db.session.delete(delete_blog)
    db.session.commit()
    return redirect(url_for('all_post'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
