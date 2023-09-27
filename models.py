from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    
    id = db.Column( db.Integer, primary_key=True)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)
    phone_number=db.Column(db.String)