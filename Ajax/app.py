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


from flask import Flask, render_template, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#desactiver les messages qui apparaissent a la console avec chaque modification de la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#permet d'établir une connexion avec ma base de données
# /// pour ajouter le chemin relatif vers la base de données
# //// pour ajouter le chemin absolu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#Creer la table Person et les colomnes demandées

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.Integer, default=0, nullable=False)
    age = db.Column(db.Integer, default=25, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    birth_town = db.Column(db.String(80), nullable=False)


@app.route('/')
def home():
    persons = Person.query.all()
    return render_template("home.html", persons=persons)

@app.route('/get-info/<int:id>')
def get_info(id):
    p = Person.query.get_or_404(id)
    return render_template ("infos.html", p=p)



#@app.route('/<string:name>')
#def get_person(name):
    #p = Person.query.filter_by(name=name).first_or_404()
    #return f"Les informations : {p.name},{p.sex}, {p.age}, {p.country}, {p.birth_town}"


