import json
from collections import OrderedDict
import subprocess

class SimulatorInstance:
    def __init__(self,bin_type,autoware_ip,rosbridge_server_port,proc):
        self.type = bin_type
        self.autoware_ip = autoware_ip
        self.rosbridge_server_port = rosbridge_server_port
        self.proc = proc

class InstanceManager:
    def __init__(self,setting_filepath):
        f = open(setting_filepath, 'r')
        self.exe_dict = json.load(f)
        self.instance_list = []
    def launch(self,bin_type,autoware_ip,rosbridge_server_port):
        for exe_data in self.exe_dict:
            if bin_type == exe_data['name']:
                for instance in self.instance_list:
                    if instance.autoware_ip == autoware_ip:
                        self.terminate(autoware_ip)
                proc = subprocess.Popen(exe_data['path'])
                instance = SimulatorInstance(bin_type,autoware_ip,rosbridge_server_port,proc)
                self.instance_list.append(instance)
    def terminate(self,autoware_ip):
        tmp_list = []
        for instance in self.instance_list:
            if instance.autoware_ip == autoware_ip:
                instance.proc.terminate()
            else:
                tmp_list.append(instance)
        self.instance_list = tmp_list

if __name__ == "__main__":
    pass