from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Task name")
    description = StringField("Description")
 
    class Meta:
        csrf = False