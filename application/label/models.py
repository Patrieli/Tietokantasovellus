from application import db

tasklabels = db.Table('tasklabels',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('label_id', db.Integer, db.ForeignKey('label.id')))

class Label(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name