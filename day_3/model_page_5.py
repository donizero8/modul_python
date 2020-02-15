from app import db

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Puppy {} is {} year/s old'.format(self.name, self.age)

    def __repr__(self):
        return '<Puppy: {}>'.format(self.name)