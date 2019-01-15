import json
from collections import OrderedDict
import subprocess
import uuid

import os

class SimulatorInstance:
    def __init__(self,bin_type,proc,instance_id):
        self.type = bin_type
        self.proc = proc
        self.instance_id = instance_id

class InstanceManager:
    def __init__(self,setting_filepath):
        f = open(setting_filepath, 'r')
        self.exe_dict = json.load(f)
        self.instance_list = []
    def launch(self,bin_type):
        for exe_data in self.exe_dict:
            if bin_type == exe_data['name']:
                config_path = os.getcwd() + '/configure.yaml'
                cmd = exe_data['path'] + ' --config' + ' ' + config_path
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                instance_id = uuid.uuid4()
                instance = SimulatorInstance(bin_type,proc,instance_id)
                self.instance_list.append(instance)
                return instance_id
    def terminate(self,instance_id):
        for instance in self.instance_list:
            if str(instance_id) == str(instance.instance_id):
                print("terminate instance id " + str(instance_id))
                instance.proc.terminate()

if __name__ == "__main__":
    pass