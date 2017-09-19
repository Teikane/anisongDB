from flask import render_template, flash, redirect, session, abort, g
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, login_manager
from .forms import LoginForm, SignupForm
from .tabledef import User
from .saltyhash import *

@login_manager.user_loader
def load_user(id):
	if id is None or id == 'None': 
		id =-1
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	user = g.user
	return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()

	# If form is valid then flash message after redirect
	if form.validate_on_submit():

		query = query(User).filter(User.username.in_([form.username.data]))
		uname_combo = query.first()

		query = query(User).filter(User.email.in_([form.username.data]))
		email_combo = query.first()

		if uname_combo and check_password(form.password.data, uname_combo.password):
			login_user(uname_combo, remember=True)
			session['remember_me'] = form.remember_me.data

		elif email_combo and check_password(form.password.data, email_combo.password):
			login_user(email_combo, remember=True)
			session['remember_me'] = form.remember_me.data

		else:
			flash ('Please check username and password.')
		return redirect(url_for('index'))
	return render_template('login.html', 
							title = 'Log In', 
							form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm()

	# If form is valid then flash message after redirect
	if form.validate_on_submit():
		# check database for existing email and user name
		query = query(User).filter(User.email.in_([form.email.data]))
		unqEmail = query.first()

		query = query(User).filter(User.username.in_([form.username.data]))
		unqUser = query.first()

		if unqEmail:
			flash('Email in use.')
		elif unqUser:
			flash('Username in use.')
		else:
			flash ('Here')

			new_user = User(form.email.data, form.username.data, hash_password(form.password.data), level=1)

			s.add(new_user)
			s.commit()

		return redirect(url_for('index'))
	return render_template('signup.html', 
							title = 'Sign up', 
							form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
