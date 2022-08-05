"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = StringField("Species",
                        validators =[AnyOf(values = ['cat', 'dog', 'porcupine'],
                        message='Only cat, dog, or porcupine', values_formatter=None)])
    photo_url = StringField("Photo URL",
                        validators =[URL(require_tld=True, message='please enter valid url')])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'), ('adult',
                      'Adult'), ('senior', 'Senior')],
                      validators =[AnyOf(values = ['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing current pet."""

    photo_url = StringField("Photo URL",
                        validators =[Optional(),
                        URL(require_tld=True, message='please enter valid url')])
    notes = StringField("Notes")
    available = SelectField("Available",
                      choices=[(True, 'Available'), (False, 'Not Available')],
                      coerce=bool,
                      validators =[AnyOf(values = [True, False])])


