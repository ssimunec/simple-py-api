from flask_cors import CORS
from flask import Flask, jsonify
import pymongo

app = Flask(__name__)
CORS(app)

konekcija_na_bazu = pymongo.MongoClient("mongodb://10.0.0.21:27017",
                                        username='root',
                                        password='123')

baza = konekcija_na_bazu["mydatabase"]
kolekcija = baza["customers"]


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return jsonify({
        'version': '0.0.1b',
        'response': 'hello world from API !',
        'status': 'sucess'
    }), 200


@app.route('/insert', methods=['POST'])
def insert():

    moj_rekors = {"name": "John", "address": "Highway 37"}

    x = kolekcija.insert_one(moj_rekors)

    return jsonify({
        'version': '0.0.1b',
        'response': 'record added',
        'status': 'sucess'
    }), 200


@app.route('/select', methods=['GET'])
def select():

    moji_rekordi = kolekcija.find()

    lista = []

    for x in moji_rekordi:
        lista.append({"name": x["name"], "address": x["address"]})

    return jsonify({
        'version': '0.0.1b',
        'response': lista,
        'status': 'sucess'
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8004)
