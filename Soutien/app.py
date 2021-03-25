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
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

#Une BD vide est disponible pour vos tests

class Declarations(db.Model):
    #TODO : arranger les types des données

    id = db.Column(db.Integer, primary_key=True)
    num_declaration = db.Column(db.BigInteger, nullable=False)
    date_declaration = db.Column(db.String(120), nullable=False, default=datetime.utcnow)
    date_insp_vispre = db.Column(db.String(120), nullable=False)
    nbr_extermin = db.Column(db.Integer, nullable=True)
    date_debuttrait = db.Column(db.String(120), nullable=True)
    date_fintrait = db.Column(db.String(120), nullable=True)
    n_qr = db.Column(db.String(20), nullable=False)
    nom_qr = db.Column(db.String(60), nullable=False)
    nom_arrond = db.Column(db.String(120), nullable=False)
    coord_x = db.Column(db.String(20), nullable=False)
    coord_y = db.Column(db.String(20), nullable=False)
    longitude = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.String(20), nullable=False) 
