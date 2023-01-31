import sys, os
sys.path.append(os.path.join(__file__))

from data_classes import Big_Container

def main():
    c = Big_Container()
    print(c)
    for container_name in c.containers :
        print(container_name)
        print(c.containers[container_name])
        # print(mc_val)

if __name__ == '__main__':
    main()