from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zfedlfzr:ecI4uOI9VI-Q7e4RRGhfHXMKQWoKQ1e7@fanny.db.elephantsql.com/zfedlfzr'
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    f_name = db.Column('f_name', db.Unicode)
    l_name = db.Column('l_name', db.Unicode)
    email = db.Column('email', db.Unicode)
    phone_number = db.Column('phone_number', db.Unicode)
    score = db.Column('score', db.Float)

    def __init__(self,user_id, f_name, l_name, email, phone_number, score):
        self.user_id = user_id
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.phone_number = phone_number
        self.score = score

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('user_id', 'f_name', 'l_name', 'email', 'phone_number', 'score')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/get_score/', methods = ['GET'])
def get_score():
    users = Users.query.with_entities(Users.user_id, Users.f_name, Users.l_name, Users.score).order_by(Users.score.desc()).all()
    result = products_schema.dump(users)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)