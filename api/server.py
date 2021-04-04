from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return jsonify({
        'version': '0.0.1b',
        'response': 'hello world from API !',
        'status': 'sucess'
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8004)
