# coding: utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/run', methods=['POST'])
def face_info():
    if request.headers['Content-Type'] != 'application/json':
        return flask.jsonify(res='error'), 400
    return flask.jsonify(res='ok')

@app.route('/api/delete', methods=['POST'])
def face_info():
    if request.headers['Content-Type'] != 'application/json':
        return flask.jsonify(res='error'), 400
    return flask.jsonify(res='ok')


if __name__ == '__main__':
    app.run()