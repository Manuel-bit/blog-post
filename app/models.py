from . import db

class Writter(db.Model):
  __tablename__ = 'wsers'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  bio= db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)