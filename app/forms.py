from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ListForm(FlaskForm):
    list_name = StringField('List Name', validators=[DataRequired()])
    add_list = SubmitField('Add List')