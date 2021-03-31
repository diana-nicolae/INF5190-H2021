from flask import Flask, jsonify, g, request
from database import Database
from livre import Livre, insert_schema
from flask_json_schema import JsonSchema,JsonValidationError
import json


app = Flask(__name__)
#assurer le bon encodage des sorties json
app.config['JSON_AS_ASCII'] = False

schema = JsonSchema(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

@app.errorhandler(404)
def page_not_found(error):
    return ("<h1> Le livre n'existe pas</h1>"), 404

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400

@app.route('/api/livres', methods=["GET"])
def get_livres():
    livres = get_db().get_livres()
    return jsonify([livre.min_info_dictionnary() for livre in livres])

@app.route('/api/livre/<int:id>', methods=["GET"])
def get_livre(id):
    livre = get_db().get_livre(id)
    if livre is None:
        return "", 404
    else:
        return jsonify(livre.all_info_dictionnary())


@app.route('/api/livre', methods=["POST"])
@schema.validate(insert_schema)
def create_livre():
    data = request.get_json()
    livre = Livre(None, data["titre"], data["auteur"], data["annee_publication"], data["nbr_pages"], data["nbr_chapitres"])
    livre = get_db().set_livre(livre)
    return jsonify(livre.min_info_dictionnary()), 201 

@app.route('/api/livre/<int:id>', methods=["DELETE"])
def delete_livre(id):
    livre = get_db().get_livre(id)
    if livre is None:
        return "", 404
    else:
        get_db().delete_livre(livre)
        return "", 200