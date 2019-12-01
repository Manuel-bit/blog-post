from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,TextAreaField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from ..models import Blog

class NewBlogForm(FlaskForm):
  title=StringField('Title',validators=[DataRequired()])
  author=StringField('Author Name',validators=[DataRequired()])
  blog=TextAreaField('My Blog',validators=[DataRequired()])
  submit=SubmitField('Save Blog')

class CommentForm(FlaskForm):
  comment = StringField('-',[validators.DataRequired()])
  Submit=SubmitField('comment')