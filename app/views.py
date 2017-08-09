from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, SignupForm

@app.route('/')
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
		return redirect('/index')
	return render_template('login.html', 
							title = 'Log In', 
							form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm()

	# If form is valid then flash message after redirect
	if form.validate_on_submit():
		flash('Signup requested for Username="%s", Password="%s" confrim Password= "%s", email="%s"' %
			(form.username.data, form.password.data, form.confirm_password.data, form.email.data))
		return redirect('/index')
	return render_template('signup.html', 
							title = 'Sign up', 
							form=form)
