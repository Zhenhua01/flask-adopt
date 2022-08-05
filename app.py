"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def load_home_page():
    """Shows home page with pets list."""

    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)

@app.route('/add', methods = ["GET", "POST"])
def show_add_pet_form():
    """Shows add pet form, accepts pet data and adds to database."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} to the database")
        return redirect("/")

    return render_template('addpetform.html', form=form)


@app.route('/<int:id>', methods = ["GET", "POST"])
def show_edit_pet_form(id):
    """Shows pet information, accepts changes, and updates database"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Pet {pet.name} was updated!")
        return redirect(f"/{id}")

    else:
        return render_template("petinfo.html", form=form, pet=pet)
