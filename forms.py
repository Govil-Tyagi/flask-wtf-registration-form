from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    
    email=StringField("Email",validators=(DataRequired(),Email()))
    
    password=PasswordField("password",validators=([DataRequired(),Length(min=6)]))
    submit=SubmitField("Register")