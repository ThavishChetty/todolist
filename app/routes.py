from flask import render_template, url_for
from app import app
from app.forms import ListForm


@app.route('/')
@app.route('/index')
def index():
	user  = {'username': 'Thavish'}
	return render_template('index.html', user=user)


@app.route('/second_page', methods=['GET', 'POST'])
def second_page():
	form = ListForm()
	user = {'username': 'Thavish'}
	return render_template('second_page.html', user=user, form=form)