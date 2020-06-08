from application import db, bcrypt
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "user"
  
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    tasks = db.relationship("Task", backref='user', lazy=True)
    projects = db.relationship("Project", backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True