from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    remember_me=BooleanField("Recordarme")
    submit=SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    password_confirm=PasswordField("Confirma tu password", validators=[DataRequired()])
    submit=SubmitField("Registrarse")

class CursoForm(FlaskForm):
    name = StringField("Nombre del curso", validators=[DataRequired()])
    submit=SubmitField("Agregar Curso")