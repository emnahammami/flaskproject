from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import validators, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('valider')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class SuprimForm(FlaskForm):
    reference = StringField('Reference',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Suprimer')


    
class AjoutForm(FlaskForm):
       submit = SubmitField('Ajouteraupanier')


       
class ApForm(FlaskForm):
    ref = StringField('Ref',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Acheter')


        
class AchatForm(FlaskForm):
       submit = SubmitField('Acheter')

class SaveForm(FlaskForm):
  ref = StringField('Ref',validators=[DataRequired(), Length(min=2, max=20)])
  nominstr = StringField('Nominstr',validators=[DataRequired(), Length(min=2, max=20)])
  prix = StringField('Prix', validators=[DataRequired(), Length(min=2, max=20)])
  image = StringField('Image',validators=[DataRequired(), Length(min=1, max=20)])
  lieufab = StringField('Lieufab',validators=[DataRequired(), Length(min=2, max=20)])
  quantiteinit = StringField('Quantiteinit',validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('Ajouter')


class ModifForm(FlaskForm):
  ref = StringField('Ref',validators=[DataRequired(), Length(min=2, max=20)])

  prix = StringField('Prix', validators=[DataRequired(), Length(min=2, max=20)])

  submit = SubmitField('Modifier')



  

