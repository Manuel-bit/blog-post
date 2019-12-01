from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,BooleanField
from wtforms.validators import EqualTo,DataRequired
from wtforms import ValidationError
from ..models import Blog

class NewBlogForm(FlaskForm):
  title=StringField('Title',validators=[DataRequired()])
  author=StringField('Author Name',validators=[DataRequired()])
  blog=TextAreaField('My Blog',validators=[DataRequired()])
  submit=SubmitField('Save Blog')