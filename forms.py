"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = SelectField("Species",
                        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine',
                        'Porcupine')],
                        validators =[InputRequired()])
    photo_url = StringField("Photo URL",
                        validators =[Optional(),
                        URL(require_tld=True, message='please enter valid url')])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'), ('adult',
                      'Adult'), ('senior', 'Senior')])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing current pet."""

    photo_url = StringField("Photo URL",
                        validators =[Optional(),
                        URL(require_tld=True, message='please enter valid url')])
    notes = StringField("Notes")
    available = BooleanField("Available", false_values=None)


