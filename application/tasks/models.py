from application import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    state = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), 
    onupdate=db.func.current_timestamp())
    deadline = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.state = "To do"
        self.active = False
        self.archived = False
        self.description = description
