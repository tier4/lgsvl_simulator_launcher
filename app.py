# coding: utf-8
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

import instance_manager
import request_parser

app = Flask(__name__)
bootstrap = Bootstrap(app)

manager = instance_manager.InstanceManager("setting.json")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulator/launch', methods=['POST'])
def launch():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error',description='failed to parse as json string'), 400
    parser = request_parser.LaunchRequestParser()
    result = parser.parse(request.json)
    if result == False:
        return jsonify(res='error',description='failed to get simulator params from json string'), 400
    parser.write()
    instance_id = manager.launch(request.json['bin_type'],parser.getIpList())
    return jsonify(res='ok',instance_id=instance_id)

@app.route('/simulator/terminate', methods=['POST'])
def terminate():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    manager.terminate(request.json['instance_id'])
    return jsonify(res='ok')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)