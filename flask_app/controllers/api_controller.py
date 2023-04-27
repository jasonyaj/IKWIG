from flask import json, jsonify, request
from flask_app import app
from flask_app.models.cars_model import Car
from flask_cors import cross_origin

@app.route('/api/cars', methods=['GET'])
@cross_origin(origins = ['http://127.0.0.1:5000'])
def api_get_all():
    list_of_cars = Car.api_get_all()
    return (jsonify(list_of_cars), 200)