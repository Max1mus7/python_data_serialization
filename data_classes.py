from collections import namedtuple
import sys, os, json

from json import JSONEncoder

from typing import Dict, List



sys.path.append(os.path.join(__file__))

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return json.dumps(obj.__dict__)



class Small_Container:
    def __init__(self, data1: str = "some data") -> None:
        self.data1 = data1

    def __iter__(self):
        yield from {
            "data": self.data1
        }

    def __str__(self):
        return json.dumps(self.__dict__)

class Big_Container:
    def __init__(self, containers: Dict[str, List[Small_Container]] = {"Containers": [Small_Container(), Small_Container("Some other data")], "Other Containers": [Small_Container(())]}) -> None:
        self.containers = containers

    def __iter__(self):
        yield from {
            "containers": self.containers
        }

    def __str__(self):
        return json.dumps(self.__dict__, default = lambda o: o.__dict__, indent=4)
    
    
def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())