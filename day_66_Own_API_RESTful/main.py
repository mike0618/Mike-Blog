from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

"""
Documentation page: https://documenter.getpostman.com/view/15802327/UVC6i6iT
"""
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    count = Cafe.query.count()
    random_id = randint(1, count)
    random_cafe = Cafe.query.get(random_id)
    # return jsonify(cafe={
    #     # 'id': random_cafe.id,
    #     'name': random_cafe.name,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'amenities': {
    #         'seats': random_cafe.seats,
    #         'has_toilet': random_cafe.has_toilet,
    #         'has_wifi': random_cafe.has_wifi,
    #         'has_sockets': random_cafe.has_sockets,
    #         'can_take_calls': random_cafe.can_take_calls,
    #         'coffee_price': random_cafe.coffee_price}})
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    loc = request.args.get('loc')
    found_cafe = db.session.query(Cafe).filter_by(location=loc).first()
    if found_cafe:
        return jsonify(cafe=[found_cafe.to_dict()])
    return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    api_key = request.form.get('api-key')
    if api_key == 'TopSecretAPIKey':
        new_cafe = Cafe(name=request.form.get("name"),
                        map_url=request.form.get("map_url"),
                        img_url=request.form.get("img_url"),
                        location=request.form.get("location"),
                        has_sockets=bool(request.form.get("has_sockets")),
                        has_toilet=bool(request.form.get("has_toilet")),
                        has_wifi=bool(request.form.get("has_wifi")),
                        can_take_calls=bool(request.form.get("can_take_calls")),
                        seats=request.form.get("seats"),
                        coffee_price=request.form.get("coffee_price"), )
        db.session.add(new_cafe)
        db.session.commit()
        print(new_cafe.name, new_cafe.map_url)
        return jsonify(response={'success': 'Successfully added the new cafe.'})
    return jsonify(error={'Forbidden': "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_price(id):
    cafe = Cafe.query.get(id)
    print(db.session.query_property())
    if cafe:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(success='Successfully updated the price.')
    return jsonify(error={'Not found': 'Sorry a cafe with that id was not found in the database.'}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:id>', methods=['DELETE'])
def delete_cafe(id):
    cafe = db.session.query(Cafe).get(id)
    if cafe:
        api_key = request.args.get('api-key')
        if api_key == 'TopSecretAPIKey':
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success=f'The {cafe.name} is successfully deleted.')
        return jsonify(error={'Forbidden': "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    return jsonify(error={'Not Found': "Sorry, a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
