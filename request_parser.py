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

if __name__ == "__main__":
    pass