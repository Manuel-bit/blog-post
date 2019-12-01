from flask import render_template,redirect,url_for
from . import auth
from ..models import Writter
from .. import db
from .forms import SignupForm

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  form=SignupForm()
  if form.validate_on_submit():
    writter = Writter(username=form.username.data,email=form.email.data)
    writter.password(form.password.data)
    db.session.add(writter)
    db.session.commit()
    return redirect(url_for('main.index'))
  return render_template('auth/signup.html',title='Sign Up',form=form)

@main.route('/login')
def login():
  return render_template('auth/login.html',title='Log In')
  