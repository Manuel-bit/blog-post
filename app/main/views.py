from flask import render_template,redirect,url_for
from . import main
from .. import db
from .forms import NewBlogForm,CommentForm
from ..models import Blog,Comment,Quotes
from flask_login import login_required,current_user 
from app.request import GetQuotes

@main.route('/')
def index():
  quotes = GetQuotes()
  print(quotes)
  return render_template('main/index.html',title="Home",quotes=quotes)

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

@main.route('/comment/<id>',methods=['GET','POST'])
def comment(id):
  writter=current_user.id
  blog=Blog.query.filter_by(id=id).first()
  if form.validate_on_submit():
    cmt = Comment(comment=form.comment.data,writter_id=writter,blog_id=id)
    db.session.add(cmt)
    db.session.commit()
    comments = Comment.query.filter_by(pitch_id=id).all()
    return render_template('comment.html',pitch=pitch,form=form,commenst=comments)
  comments = Comment.query.filter_by(pitch_id=id).all()
  return render_template('comment.html',form=form,pitch=pitch,comments=comments)
