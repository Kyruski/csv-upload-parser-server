from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/file', methods=['POST'])
def parseFile():
    f = request.files['File']
    return f.filename


if __name__ == "__main__":
    app.run(debug=True)
