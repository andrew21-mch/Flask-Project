from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#registration form
class RegistrationForm(FlaskForm):
    firstName = StringField('first Name', validators=[DataRequired()])
    lastName = StringField('last Name', validators=[DataRequired()])
    username = StringField('username',validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired(), Length(min=6, max=12)])
    password_repeat = PasswordField('repeat password',validators=[DataRequired(), Length(min=6, max=12),EqualTo(password)])
    submit = SubmitField('signup')

#login form
class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    

