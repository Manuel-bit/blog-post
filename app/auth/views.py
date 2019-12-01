from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import Writter
from .. import db
from .forms import SignupForm,LoginForm
from flask_login import login_user, current_user,logout_user

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  form=SignupForm()
  if form.validate_on_submit():
    writter = Writter(username=form.username.data,email=form.email.data)
    writter.password(form.password.data)
    db.session.add(writter)
    db.session.commit()
    return redirect(url_for('auth.login'))
  return render_template('auth/signup.html',title='Sign Up',form=form)

@auth.route('/login',methods = ["GET","POST"])
def login():
  form=LoginForm()
  if form.validate_on_submit():
    writter=Writter.query.filter_by(username = form.username.data).first()
    if writter != None and writter.verify_password(form.password.data):
      login_user(writter,form.remember.data)
      return redirect(url_for('main.index'))
    flash('invalid username or password')
  return render_template('auth/login.html',title='Log In',form=form)

@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))