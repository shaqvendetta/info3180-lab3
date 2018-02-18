from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,validators, ValidationError, TextField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    name = StringField('Name',validators = [DataRequired()])
    email = TextField('Email', [validators.DataRequired(), validators.Email("Please enter a valid email")])
    subject = StringField('Subject', validators = [DataRequired()])
    message = StringField('Message', validators = [DataRequired()])
    