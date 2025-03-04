from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import ListForm
from app.models import List
import sqlalchemy as sa


@app.route('/')
@app.route('/index')
def index():
	user  = {'username': 'Thavish'}
	return render_template('index.html', user=user)


@app.route('/second_page', methods=['GET', 'POST'])
def second_page():
	user  = {'username': 'Thavish'}
	form = ListForm()
	if form.validate_on_submit():
		todolist = List(listname=form.list_name.data) 
		db.session.add(todolist)
		db.session.commit()
		flash('Congratulations, you added the list:  %s' % (form.list_name.data))
		return redirect(url_for('index'))
	return render_template('second_page.html', form=form, user=user)


@app.route('/lists', methods=['GET'])
def lists():
	user  = {'username': 'Thavish'}
	query = sa.select(List).order_by(List.listname.asc())
	todolists = db.session.scalars(query).all()
	return render_template('lists.html', user=user, lists=todolists)