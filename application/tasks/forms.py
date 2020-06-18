from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=3, max=30), validators.data_required()])
    description = StringField("Description", [validators.Length(max=144)])
    deadline = DateField('Deadline', format='%d/%m/%Y')
    labels = StringField("Labels")
 
    class Meta:
        csrf = False

class TaskEditForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=3, max=30), validators.data_required()])
    description = StringField("Description", [validators.Length(max=144)])
    deadline = DateField('Deadline', format='%d/%m/%Y')
    status = SelectField('Status', choices=[('To-do', 'To do'), ('In progress', 'In progress'), ('Completed', 'Completed')])
    labels = StringField("Labels")
 
    class Meta:
        csrf = False