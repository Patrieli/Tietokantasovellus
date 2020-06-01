from application import db
from application.models import Base

from sqlalchemy.sql import text

class Task(Base):
    name = db.Column(db.String(144), nullable=False)
    state = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    labels = db.relationship('Label', secondary='tasklabels', backref=db.backref('tasks'), lazy=True)

    def __init__(self, name, description, deadline):
        self.name = name
        self.state = "To-do"
        self.active = False
        self.archived = False
        self.description = description
        self.deadline = deadline

    @staticmethod
    def list_all_completed_tasks(user_id):
        stmt = text("SELECT id, name, description, date_modified, state FROM Task " 
                    "WHERE (state = 'Completed') AND (user_id = :user_id)").params(user_id = user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "description":row[2], "date_modified":row[3], "state":row[4]})
        return response

    @staticmethod
    def count_all_tasks(user_id):
        stmt = text("SELECT state, COUNT(id) AS count FROM Task "
                    "WHERE (user_id = :user_id) "
                    "GROUP BY state").params(user_id = user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"state":row[0], "count":row[1]})

        return response
