import pyeapi
import pprint
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

def d_usage(hostip):
    node = pyeapi.connect(transport="https", host=hostip, username="admin", password="n51ght!", port=443)
    node.transport._context.set_ciphers('DEFAULT') 
    print(f"{bcolors.RED}\nConnecting to Node", hostip)
    #print(node)
    status = node.execute(["bash timeout 1 df -kh"])
    header = status["result"][0]["messages"][0].split("\n")[0]
    flash = status["result"][0]["messages"][0].split("\n")[1]
    print(f"{bcolors.CYAN}", header)
    print(f"{bcolors.YELLOW}", flash,f"{bcolors.WHITE}")


switches = ["10.1.1.69", "10.1.1.148","10.1.1.58"]
for switch in switches:
    d_usage(switch)
