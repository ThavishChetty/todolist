from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import sqlalchemy as sa
from app import db
from app.models import List

class ListForm(FlaskForm):
    list_name = StringField('List Name', validators=[DataRequired()])
    add_list = SubmitField('Add List')


    def validate_listname(self, list_name):
        todolist = db.session.scalar(sa.select(List).where(
            List.listname == list_name.data))
        if todolist is not None:
            raise ValidationError('Please use a different name for the list.')
