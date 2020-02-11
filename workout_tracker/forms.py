from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddForm(FlaskForm):
    exercise = StringField('Exercise', validators=[DataRequired(), Length(min=2, max=20)])
    weight = StringField('Weight',validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Send')
