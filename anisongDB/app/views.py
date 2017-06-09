from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	# Create fake user and render home page template
	user ={'nickname': 'admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Log In', form=form)
