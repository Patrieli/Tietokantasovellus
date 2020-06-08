from application import db
from application.models import Base

from sqlalchemy.sql import text

class Project(Base):
    name = db.Column(db.String(30), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    tasks = db.relationship("Task", backref='project', lazy=True)

    def __init__(self, name):
        self.name = name
        self.active = False