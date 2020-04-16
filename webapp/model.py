from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()


class electro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t1 = db.Column(db.Integer)
    t2 = db.Column(db.Integer)
    tarif1 = db.Column(db.Integer)
    tarif2 = db.Column(db.Integer)
    summ = db.Column(db.Integer)

    date = db.Column(db.String(150))