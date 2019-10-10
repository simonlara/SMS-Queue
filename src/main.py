"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from queue_datastructure import Queue
from models import db
Queue=Queue()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/new', methods=['POST'])
def handle_new():
    new=request.get_json()
    if 'name' not in new:
        return 'falta nombre',400
    if 'phone' not in new:
        return 'falta numero',400
    respuesta=Queue.enqueue(new)

    return jsonify(respuesta), 200

@app.route('/next', methods=['GET'])
def handle_next():

    respuesta=Queue.dequeue()

    return jsonify(respuesta), 200

@app.route('/all', methods=['GET'])
def handle_all():

    respuesta=Queue.get_all()

    return jsonify(respuesta), 200

# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
