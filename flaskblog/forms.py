from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	username=StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password',validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')])
	submit= SubmitField('Sign up')
	def validate_field(self,field):
		if True:
			raise ValidationError('Validation message')
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one')
	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')
	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')
class LoginForm(FlaskForm):
	email =StringField('Email', validators = [DataRequired(),Email()])
	password = PasswordField('Password',validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit= SubmitField('Log in')


