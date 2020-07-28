import json

class Demo():

    def add(self, a,b):
        return a + b

    #Almost like read file
    def read_json(self, file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    