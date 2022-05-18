from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4y7sV96vA9wv46VR@192.168.100.10:5432/names'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, Name: {self.name}>'


class Customer(db.Model):

    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    gender = db.Column(db.String)
    ip_address = db.Column(db.String)

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


@app.route('/')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
