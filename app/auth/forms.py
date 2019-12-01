from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,BooleanField
from wtforms.validators import EqualTo,DataRequired
from wtforms import ValidationError