from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
API_KEY="3c045b5479d3bb7b3e74b9fb6ca6fe1f"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
count=0
class Bass():
    pass
db=SQLAlchemy(model_class=Bass)
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///list_of_movies.db"
bootstrap=Bootstrap5(app)
db.init_app(app)
class Movies(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column()
    year:Mapped[str]=mapped_column()
    description:Mapped[str]=mapped_column()
    rating:Mapped[int]=mapped_column()
    ranking:Mapped[str]=mapped_column()
    review:Mapped[str]=mapped_column()
    img_url:Mapped[str]=mapped_column()



with app.app_context():
    db.create_all()

class Myform(FlaskForm):
    rating=StringField('Youre Rating out of 10 e.g 7.5',validators=[DataRequired()])
    review=StringField("You're Review ",validators=[DataRequired()])
    done=SubmitField("Done")
class My_add(FlaskForm):
    add_movies=StringField('Movie Title',validators=[DataRequired()])
    done=SubmitField('Done',validators=[DataRequired()])
app.secret_key="dkvzvjj"
@app.route("/")
def home():
    all_data = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().all()
    print(len(all_data))
    for i in range(len(all_data)):
        all_data[i].ranking = len(all_data) - i
    return render_template("index.html",all_data=all_data,counts=count)
@app.route("/edit<int:index>",methods=["post","get"])
def edit(index):
    form=Myform()
    update = db.get_or_404(Movies, index)
    if form.validate_on_submit():
        update.review=form.review.data
        update.rating=form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=form,all_data=update)
@app.route("/delete/<int:index>")
def delete(index):
    delete_this_movies=db.get_or_404(Movies,index)
    db.session.delete(delete_this_movies)
    db.session.commit()
    return redirect(url_for('home'))
@app.route("/add",methods=["post","get"])
def add():
    form=My_add()
    if form.validate_on_submit():
        name=form.add_movies.data
        url = "https://api.themoviedb.org/3/search/movie"
        paramas = {
            "query": name,
            "api_key": API_KEY


        }
        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers, params=paramas)

        all_search = response.json()["results"]
        return render_template('select.html',searched=all_search)
    return render_template("add.html",form=form)
@app.route("/find")
def submit():
    movie_api_id = request.args.get("data")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movies(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            rating=float(data['vote_average']),
            ranking="None",
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
            review="None"
        )
        db.session.add(new_movie)
        db.session.commit()
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
