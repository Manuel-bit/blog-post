from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return Writter.query.get(int(user_id))

class Writter(db.Model,UserMixin):
  __tablename__ = 'writters'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  bio= db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  blogs=db.relationship('Blog',backref = 'writter',lazy='dynamic')
  
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

class Blog(db.Model):
  __tablename__='blogs'
  id= db.Column(db.Integer,primary_key=True)
  author=db.Column(db.String(255))
  title=db.Column(db.String(255))
  blog= db.Column(db.String(2000))
  blog_image=db.column(db.String(255))
  writter_id=db.Column(db.Integer, db.ForeignKey('writters.id'))

class Comment(db.Model):
  __tablename__='comments'
  id=db.Column(db.Integer, primary_key=True)
  comment=db.Column(db.String(255))
  blog_id=db.Column(db.Integer, db.ForeignKey('blogs.id'))
  writter_id = db.Column(db.Integer, db.ForeignKey('writters.id'))

class Quotes:
  def __init__(self,author,randomquote):
    self.author = author
    self.quote = randomquote