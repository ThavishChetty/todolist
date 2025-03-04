from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    user  = {'username': 'Thavish'}
    return render_template('404.html', user=user), 404

@app.errorhandler(500)
def internal_error(error):
    user  = {'username': 'Thavish'}
    db.session.rollback()
    return render_template('500.html', user=user), 500