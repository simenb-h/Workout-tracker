from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime


class AddForm(FlaskForm):
    exercise = StringField('Exercise', validators=[DataRequired(), Length(min=2, max=20)])
    weight = StringField('Weight',validators=[DataRequired()])
    category = SelectField('Category', choices=[('arms', 'Arms'), ('legs', 'Legs'), ('stomach', 'Stomach')])
    #date_posted = DateField('Date', format='%d-%m-%Y', default=datetime.utcnow)
    submit = SubmitField('Send')
