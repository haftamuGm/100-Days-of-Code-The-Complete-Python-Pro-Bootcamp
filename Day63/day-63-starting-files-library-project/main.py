from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,FLOAT
app=Flask(__name__)
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
db=SQLAlchemy(model_class=Base)
db.init_app(app)
class Book(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(unique=False)
    author:Mapped[str]=mapped_column(nullable=False)
    review:Mapped[str]=mapped_column(nullable=False)
with app.app_context():
    db.create_all()
@app.route("/")
def home():
    result=db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html",all_book=result)

@app.route("/add",methods=["POST","get"])
def add():
    if request.method=="POST":
        user=Book(
            title=request.form["title"],
            author=request.form["author"],
            review=request.form["rating"],

             )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")
@app.route("/<int:index>")
def edit(index):
    edit_values=db.session.execute(db.select(Book).where(Book.id==index)).scalar()
    return render_template("editing.html",all_data=edit_values)
@app.route("/ed",methods=["POST","GET"])
def edit_change():
    if request.method=="POST":
        id=request.form["id"]
        update=db.get_or_404(Book,id)
        update.review=request.form["rate"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("editing.html")

@app.route("/delete<int:index>")
def delete(index):
    delete_list=db.session.execute(db.select(Book).order_by(Book.id==index)).scalar()
    db.session.delete(delete_list)
    db.session.commit()
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)
