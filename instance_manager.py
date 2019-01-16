import json
from collections import OrderedDict
import subprocess
import uuid

import os

class SimulatorInstance:
    def __init__(self,bin_type,proc,instance_id,ip_list):
        self.type = bin_type
        self.proc = proc
        self.instance_id = instance_id
        self.ip_list = ip_list

class InstanceManager:
    def __init__(self,setting_filepath):
        f = open(setting_filepath, 'r')
        self.exe_dict = json.load(f)
        self.instance_list = []
    def launch(self,bin_type,ip_list):
        for exe_data in self.exe_dict:au
            if bin_type == exe_data['name']:
                for autoware_address in ip_list:
                    result = self.isAlreadyExist(autoware_address)
                    if result["result"]:
                        return result["instance_id"]
                config_path = os.getcwd() + '/configure.yaml'
                cmd = exe_data['path'] + ' --config' + ' ' + config_path
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                instance_id = uuid.uuid4()
                instance = SimulatorInstance(bin_type,proc,instance_id,ip_list)
                self.instance_list.append(instance)
                return instance_id
    def terminate(self,instance_id):
        new_instance_list = []
        for instance in self.instance_list:
            if str(instance_id) == str(instance.instance_id):
                print("terminate instance id " + str(instance_id))
                instance.proc.terminate()
            else:
                new_instance_list.append(instance)
        self.instance_list = new_instance_list
    def isAlreadyExist(self,ip_address):
        for instance in self.instance_list:
            for autoware_address in instance.ip_list:
                if str(autoware_address) == str(ip_address):
                    return {"result" : True, "instance_id" : instance.instance_id}
        return {"result" : False}

if __name__ == "__main__":
    pass