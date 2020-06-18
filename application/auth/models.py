from application import db, bcrypt
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "user"
  
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(5), nullable=False)

    tasks = db.relationship("Task", backref='user', lazy=True)
    projects = db.relationship("Project", backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.role = "USER"
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]

    # @staticmethod
    # def users_without_tasks():

    #     stmt = text("SELECT User.id, User.username, User.role FROM User"
    #                 " LEFT JOIN Task ON User.id = Task.user_id"
    #                 " WHERE Task.user_id IS NULL")
        
    #     res = db.engine.execute(stmt)

    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "username":row[1], "role":row[2]})

    #     return response

    @staticmethod
    def task_count(user_id):
        stmt = text("SELECT COUNT(id) AS count FROM Task "
                    "WHERE (user_id = :user_id) ").params(user_id = user_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count":row[0]})

        return response