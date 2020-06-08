from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=3, max=30)])
    description = StringField("Description", [validators.Length(max=144)])
    deadline = DateField('Deadline', format='%d/%m/%Y')
    labels = StringField("Labels")
 
    class Meta:
        csrf = False