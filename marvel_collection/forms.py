from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()


class addMarvel(FlaskForm):
    name = StringField('Superhero Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    comics_appeared_in = IntegerField(
        'Number of Comics Appeared In', validators=[DataRequired()])
    super_power = StringField('Super Power', validators=[DataRequired()])
    submit_button = SubmitField()
