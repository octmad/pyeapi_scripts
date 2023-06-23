import pyeapi
import pprint
from natsort import natsorted
import sys
import re

class bcolors:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def int_st(hostip):
    node = pyeapi.connect(transport="https", host=hostip, username="admin", password="n51ght!", port="3004")
    node.transport._context.set_ciphers('DEFAULT')
    print("Connecting to Node", hostip)
    print(node)
    status = node.execute(["show interfaces status connected"])
    #pprint.pprint(status)
    int_dict=status["result"][0]["interfaceStatuses"]
    ilist=list(int_dict.keys())
    ilist=natsorted(ilist)


    for i in range(len(int_dict)):
        inter = ilist[i]
        name=inter
        #pprint.pprint(int_dict[inter])
        Description=int_dict[inter]["description"]
        Speed=re.sub("000000000$","G",str(int_dict[inter]["bandwidth"]))
        Status=int_dict[inter]["linkStatus"]
        print(f"{bcolors.CYAN}Interface",f"{bcolors.YELLOW} {name}",f"{bcolors.CYAN}Description",f"{bcolors.YELLOW} {Description}",f"{bcolors.CYAN}Speed",f"{bcolors.YELLOW} {Speed}",
              f"{bcolors.CYAN}Status",f"{bcolors.YELLOW} {Status}")


print("Current version of Python is ", sys.version)
int_st("127.0.0.1")