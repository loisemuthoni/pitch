fro flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Confirm_Password', validators=[DataRequired()])
    Confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])