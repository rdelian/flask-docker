from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Missing Email"), Email(message="Invalid Email")])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message="Passwords must match")])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    register_key = PasswordField('Register Key', validators=[DataRequired()])
    user_id = HiddenField(validators=[DataRequired()])
