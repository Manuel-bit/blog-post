from flask import render_template
from . import auth

@auth.route('/signup')
def signup():
  return render_template('auth/signup.html',title='Sign Up')