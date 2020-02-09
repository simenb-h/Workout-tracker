from workout_tracker import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    exercise = db.Column(db.String(20), unique=True, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Post %r' % self.exercise