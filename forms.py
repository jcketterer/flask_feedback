from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, Optional


class UserForm(FlaskForm):

    username = StringField("Username", validators=[
                           InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[
                             InputRequired(), Length(min=6, max=55)])
    email = StringField("Email", validators=[
                        InputRequired(), Email(message='Please Enter A Valid Email'), Length(max=50)])
    first_name = StringField("First Name", validators=[
                             InputRequired(message='Please Enter First Name'), Length(max=30)])
    last_name = StringField("Last Name", validators=[
                            InputRequired(message='Please Enter Last Name'), Length(max=30)])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired(), Length(min=1, max=20)])
    password = PasswordField("Password", validators=[
                             InputRequired(), Length(min=6, max=55)])


class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=100)])
    content = StringField("Content", validators=[InputRequired()])


class DeleteForm(FlaskForm):
    """Meant to be left blank"""
