import nh3

from project import db, app


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = nh3.clean_text(name)
        self.city = nh3.clean_text(city)
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
