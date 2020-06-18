from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=3, max=30), validators.Regexp('[0-9A-Za-z_]+'), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=3, max=144), validators.DataRequired()])
  
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    username = StringField('Username',  [validators.Length(min=3, max=30), validators.Regexp('[0-9A-Za-z_]+'), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=3, max=144), validators.DataRequired()])
    repassword = PasswordField('Confirm password', [validators.Length(min=3, max=144), validators.DataRequired()])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    username = StringField('Username',  [validators.Length(min=3, max=30), validators.Regexp('[0-9A-Za-z_]+'), validators.DataRequired()])
    role = SelectField('Role', choices=[('USER', 'User'), ('ADMIN', 'Admin')])
    
    class Meta:
        csrf = False