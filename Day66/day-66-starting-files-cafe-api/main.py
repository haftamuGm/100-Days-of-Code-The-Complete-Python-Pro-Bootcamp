from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()
def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "map_url": self.map_url,
        "image_url": self.img_url,
        "location": self.location,
        "seats": self.seats,
        "has_toilet": self.has_toilet,
        "has_wifi": self.has_wifi,
        "has_sockets": self.has_sockets,
        "can_take_calls": self.can_take_calls,
        "coffee_price": self.coffee_price

    }
@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route("/random")
def get_random_request():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe=random.choice(result)
    return jsonify(
        {
        "id":random_cafe.id,
        "name":random_cafe.name,
        "map_url": random_cafe.map_url,
        "image_url":random_cafe.img_url,
        "location":random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,

        }
    )

@app.route("/all")
def get_all_request():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    cafes = [to_dict(random_cafe) for random_cafe in result]
    return jsonify(cafes)
@app.route("/search")
def search():
    loc = request.args.get('loc')
    all_cafe_location=db.session.execute(db.select(Cafe).where(Cafe.location==loc)).scalars().all()
    if all_cafe_location:
        cafe_location=[
            [to_dict(cafe_loc) for cafe_loc in all_cafe_location ]
        ]
        return jsonify(cafe_location)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
@app.route("/add",methods=["post"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def price_of_coffee(cafe_id):
    prices=request.args.get('price')
    update = db.get_or_404(Cafe, cafe_id)
    if update:
        update.coffee_price=prices
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
if __name__ == '__main__':
    app.run(debug=True)
