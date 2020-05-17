from application import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    state = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name
        self.state = "To do"
        self.active = False
