from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	# Create fake user and render home page template
	user ={'nickname': 'admin'}
	return render_template('index.html', title='Home', user=user)