from flask import render_template,redirect,url_for
from . import main
from .. import db
from .forms import NewBlogForm
from ..models import Blog
from flask_login import login_required,current_user 

@main.route('/')
def index():
  return render_template('main/index.html',title="Home")

@main.route('/newblog', methods =["GET", "POST"])
@login_required
def newblog():
  writter=current_user.id
  form=NewBlogForm()
  if form.validate_on_submit():
    blog= Blog(title=form.title.data, author=form.author.data,blog=form.blog.data,writter_id=writter)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.index'))
  return render_template('main/newblog.html',title='New Blog',form=form)
