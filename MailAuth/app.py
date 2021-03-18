"""
 Copyright 2021 Ela El-Heni
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, logout_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

#Generé avec : import secrets, secrets.token_hex(16)
app.config['SECRET_KEY'] = '30619d162891c7cbf8342dc2633a57b5'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mdp = db.Column(db.String(60), nullable=False)




class Inscription(FlaskForm):
    nom = StringField("Nom de l'utilisateur", validators=[DataRequired()])
    prenom = StringField("Prenom de l'utilisateur", validators=[DataRequired()])
    email = StringField("Adresse mail", validators=[DataRequired(), Email()])
    confirm_email = StringField("Validation de l'adresse mail", validators=[DataRequired(), Email(), EqualTo('email')])
    password = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Mot de passe", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("S'inscrire")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Cette adresse mail existe déjà !")

class Login(FlaskForm):
    email = StringField ('Adresse mail', validators=[DataRequired(), Email()])
    password = PasswordField ('Mot de passe', validators=[DataRequired()])
    remember = BooleanField('Se souvenir de moi')

    submit = SubmitField('Se connecter')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def home():

    form = Inscription()
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(nom=form.nom.data, prenom=form.prenom.data, email=form.email.data, mdp=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Votre compte a été créé avec succès, Vous pouvez vous connectez!', 'success')
        return redirect(url_for('login'))

    else:

        return render_template('inscription.html', form=form)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method=="POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.mdp, form.password.data):
            return redirect(f'/confirmation')
        else:
            flash('Connexion impossible, merci de vérifier votre adresse mail et votre mot de passe.', 'danger')

    else:
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Vous etes déconnecté !', 'success')
    return redirect(url_for('home'))