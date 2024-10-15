from . import db
from datetime import datetime, timezone

class User(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    gender = db.Column(db.String(15))
    dept = db.Column(db.String(15))
    role = db.Column(db.String(10))

class WellnessProgram(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100))
    pstart = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    pend = db.Column(db.DateTime,  default=datetime.now(timezone.utc))
    pvenue = db.Column(db.String(100))
    porganizer = db.Column(db.String(100))
    pdesc = db.Column(db.Text)
    pcontact = db.Column(db.String(20))

class WellnessParticipation(db.Model):
    ppid = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    status = db.Column(db.String(25))
    pregtime = db.Column(db.DateTime, default=datetime.now(timezone.utc))

