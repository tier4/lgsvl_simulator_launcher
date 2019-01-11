# coding: utf-8
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

import instance_manager

app = Flask(__name__)
bootstrap = Bootstrap(app)

manager = instance_manager.InstanceManager("setting.json")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulator/launch', methods=['POST'])
def launch():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    manager.launch(request.json['bin_type'],request.json['autoware_ip'],request.json['rosbridge_server_port'])
    return jsonify(res='ok')

@app.route('/simulator/terminate', methods=['POST'])
def terminate():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify(res='error'), 400
    return jsonify(res='ok')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)