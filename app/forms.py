from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

class LoginForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(message='Porfavor llene el campo'), Email(message='Ingrese un email valido')])
    password=PasswordField("Password", validators=[DataRequired(message='Porfavor llene el campo')])
    remember_me=BooleanField("Mantener sesión iniciada")
    submit=SubmitField("Sign In")


class RegisterForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(message='Porfavor llene el campo'), Email(message='Porfavor llene el campo')])
    password=PasswordField("Password", validators=[DataRequired(message='Porfavor llene el campo')])
    password_confirm=PasswordField("Confirma el password", validators=[DataRequired(message='Porfavor llene el campo')])
    submit=SubmitField("Register")

class CursoForm(FlaskForm):
    name = StringField("Nombre del curso", validators=[DataRequired(message='Porfavor llene el campo')])
    submit=SubmitField("Register course")

class TareaForm(FlaskForm):
    titulo = StringField("Titulo", validators=[DataRequired(message='Porfavor llene el campo')])
    fecha_de_creacion = DateTimeField("Fecha de creación (dd-mm-yyyy)",format='%d-%m-%Y', validators=[DataRequired('Llene el campo con el formato dd-mm-yyyy')] )
    fecha_de_entrega = DateTimeField("Fecha de entrega (dd-mm-yyyy)", format='%d-%m-%Y', validators=[DataRequired('Llene el campo con el formato dd-mm-yyyy')] )
    descripcion = StringField("Descripción", validators=[DataRequired('Porfavor llene el campo')])
    puntos = IntegerField("Puntos", validators=[DataRequired('Porfavor llene el campo'), NumberRange(min=0, max=100, message='Ingrese un numero entre 0 y 100')])
    submit=SubmitField("Registrar Tarea")
