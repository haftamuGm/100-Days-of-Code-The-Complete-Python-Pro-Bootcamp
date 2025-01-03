from tkinter.font import names

import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager=LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB


class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)
@app.route('/register',methods=["GET","POST"])
@login_required
def register():
    if request.method =='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        check=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if check:
            flash("This email already exit")
            return redirect(url_for('login'))
        else:
            hash_fun = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)

            new_user=User(
                name=name,
                email=email,
                password=hash_fun,

            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login',methods=["POST","GET"])
@login_required
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if  not user :
            flash("the email doesn't exit please try again")
            return redirect(url_for('login'))
        elif check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('secrets'))
        else:
            flash("Incorrect password ")
            return redirect(url_for('login'))



    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",logged_in=True)
@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User,id)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))




@app.route('/download')
@login_required
def download():
    return send_from_directory('static',"files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
