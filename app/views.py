from flask import render_template, flash, redirect, session, abort

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app
from .forms import LoginForm, SignupForm
from .tabledef import *

engine = create_engine('sqlite:///anisong.db', echo=True)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return index()
	else:
		return "Hello <a href='/logout'>Logout</a>"
@app.route('/index')
def index():
	# Create fake user and render home page template
	user ={'nickname': 'admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()

	# If form is valid then flash message after redirect
	if form.validate_on_submit():
		flash('Login requested for Username="%s", Password="%s",remember_me=%s' %
			(form.username.data, form.password.data, str(form.remember_me.data)))

		Session = sessionmaker(bind=engine)
		s = Session()

		query = s.query(User).filter(User.username.in_([form.username.data]),User.password.in_([form.password.data]))
		username_combo = query.first()

		query = s.query(User).filter(User.email.in_([form.username.data]),User.password.in_([form.password.data]))
		email_combo = query.first()

		if username_combo:
			session['logged_in'] = True
			flash ("Hello {}".format(form.username.data))

		elif email_combo:
			session['logged_in'] = True
			flash ("Hello {}".format(email_combo))

		else:
			flash ('Please check username and password.')
		return home()
	return render_template('login.html', 
							title = 'Log In', 
							form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm()

	# If form is valid then flash message after redirect
	if form.validate_on_submit():
		flash('Signup requested for email="%s", Username="%s", Password="%s" confrim Password= "%s"' %
			(form.email.data, form.username.data, form.password.data, form.confirm_password.data))

		Session = sessionmaker(bind=engine)
		s = Session()

		# check database for existing email and user name
		query = s.query(User).filter(User.email.in_([form.email.data]))
		unqEmail = query.first()

		query = s.query(User).filter(User.username.in_([form.username.data]))
		unqUser = query.first()

		if unqEmail:
			flash('Email in use.')
		elif unqUser:
			flash('Username in use.')
		else:
			flash ('Here')

			new_user = User(form.email.data, form.username.data, form.password.data)

			s.add(new_user)
			s.commit()
			s.commit()

		return redirect('/index')
	return render_template('signup.html', 
							title = 'Sign up', 
							form=form)

@app.route('/logout')
def logout():
	session['logged_in'] = False
	return home()
