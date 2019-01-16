import yaml
import json

class LaunchRequestParser:
    def __init__(self):
        self.dict = {}
    def parse(self,json):
        self.dict = json
        return True
    def write(self):
        f = open("configure.yaml", "w")
        f.write(yaml.dump(self.dict, default_flow_style=False))
    def getIpList(self):
        vehicles = self.dict["vehicles"]
        ip_lists = []
        for vehicle in vehicles:
            ip_lists.append(vehicle['address'])
        return ip_lists

if __name__ == "__main__":
    pass