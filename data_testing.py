import sys, os, json, jsonpickle
sys.path.append(os.path.join(__file__))

from data_classes import Big_Container
from data_classes import MyEncoder, customStudentDecoder

def main():
    c = Big_Container()
    print(c)
    # for container_name in c.containers :
        # print(container_name)
        # for item in c.containers[container_name]:
            # print(item)
        # print(mc_val)
        
    f = open("data.json", "w")
    f.write(jsonpickle.encode(c))
    f.close()
    
    f = open("data.json", "r")
    data = f.read()
    f.close()
    data = jsonpickle.decode(data) 
    print(data)
    # print(f"{type(c)} {type(data)}")
    print(data.containers["Containers"] == c.containers["Containers"])

if __name__ == '__main__':
    main()