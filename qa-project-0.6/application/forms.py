from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    description = StringField('Proposed Name', validators = [DataRequired()])
    
    submit = SubmitField('Add Species')