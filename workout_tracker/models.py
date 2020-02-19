from workout_tracker import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    exercise = db.Column(db.String(20), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Post %r' % self.exercise