from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
	
class SignupForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	confirm_password = PasswordField('password', validators=[DataRequired(), EqualTo('password')])
	email = StringField('password', validators=[DataRequired(), Email()])
