from flask import Flask, request, Response
from flask_cors import CORS
from pdmanipulate import read_file

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/file', methods=['POST'])
def parseFile():
    f = request.files['File']
    xAxis = request.form['xAxis']
    return read_file(f, xAxis)


if __name__ == "__main__":
    app.run(debug=True)
