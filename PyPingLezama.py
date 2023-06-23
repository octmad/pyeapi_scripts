import os
import time
import pyeapi
from datetime import datetime

# colors
# 0 is black, 2 is green, 4 is red

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

# Create a nested dictionary
machines = {'Bilbao HUB': {'Location': "Lezama5", 'IP': "192.168.68.1", 'DeviceType': "switch"},
            '720-Lezama5-1': {'Location': "Lezama5", 'IP': "192.168.68.11", 'DeviceType': "switch"},
            '720-Lezama5-2': {'Location': "Lezama5", 'IP': "192.168.68.12", 'DeviceType': "switch"},
            '720-Lezama5-3': {'Location': "Lezama5", 'IP': "192.168.68.13", 'DeviceType': "switch"},
            'SNS': {'Location': "Lezama5", 'IP': "192.168.66.31", 'DeviceType': "computer"},
            'JumpServer1': {'Location': "Lezama5", 'IP': "192.168.68.21", 'DeviceType': "computer"},
            'JumpServer2': {'Location': "Lezama5", 'IP': "192.168.68.22", 'DeviceType': "computer"},
            'MacMini': {'Location': "Lezama5", 'IP': "192.168.68.95", 'DeviceType': "computer"},
            'MacBook': {'Location': "Lezama5", 'IP': "192.168.68.97", 'DeviceType': "computer"},
            'Magewell_A': {'Location': "Lezama5", 'IP': "192.168.65.100", 'DeviceType': "camera"},
            'Magewell_B': {'Location': "Lezama5", 'IP': "192.168.65.101", 'DeviceType': "camera"},
            'Magewell_C': {'Location': "Lezama5", 'IP': "192.168.65.102", 'DeviceType': "camera"},
            'Magewell_D': {'Location': "Lezama5", 'IP': "192.168.65.103", 'DeviceType': "camera"},
            'Magewell_E': {'Location': "Lezama5", 'IP': "192.168.65.104", 'DeviceType': "camera"},
            'Magewell_F': {'Location': "Lezama5", 'IP': "192.168.65.105", 'DeviceType': "camera"},
            'Magewell_G': {'Location': "Lezama5", 'IP': "192.168.65.106", 'DeviceType': "camera"},
            'Magewell_H': {'Location': "Lezama5", 'IP': "192.168.65.107", 'DeviceType': "camera"},
            'Magewell_I': {'Location': "Lezama5", 'IP': "192.168.65.108", 'DeviceType': "camera"},
            'Magewell_J': {'Location': "Lezama5", 'IP': "192.168.65.109", 'DeviceType': "camera"},
            'Magewell_K': {'Location': "Lezama5", 'IP': "192.168.65.110", 'DeviceType': "camera"},
            'Magewell_L': {'Location': "Lezama5", 'IP': "192.168.65.111", 'DeviceType': "camera"},
            'Camera_A': {'Location': "Lezama5", 'IP': "192.168.66.200", 'DeviceType': "camera"},
            'Camera_B': {'Location': "Lezama5", 'IP': "192.168.66.201", 'DeviceType': "camera"},
            'Camera_C': {'Location': "Lezama5", 'IP': "192.168.66.202", 'DeviceType': "camera"},
            'Camera_D': {'Location': "Lezama5", 'IP': "192.168.66.203", 'DeviceType': "camera"},
            'Camera_E': {'Location': "Lezama5", 'IP': "192.168.66.204", 'DeviceType': "camera"},
            'Camera_F': {'Location': "Lezama5", 'IP': "192.168.66.205", 'DeviceType': "camera"},
            'Camera_G': {'Location': "Lezama5", 'IP': "192.168.66.206", 'DeviceType': "camera"},
            'Camera_H': {'Location': "Lezama5", 'IP': "192.168.66.207", 'DeviceType': "camera"},
            'Camera_I': {'Location': "Lezama5", 'IP': "192.168.66.208", 'DeviceType': "camera"},
            'Camera_J': {'Location': "Lezama5", 'IP': "192.168.66.209", 'DeviceType': "camera"},
            'Camera_K': {'Location': "Lezama5", 'IP': "192.168.66.210", 'DeviceType': "camera"},
            'Camera_L': {'Location': "Lezama5", 'IP': "192.168.66.211", 'DeviceType': "camera"}}

while (1):
    os.system('cls' if os.name == 'nt' else 'clear')

    f = open("corpNet DownLog.txt", "a")

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
    print(f"{bcolors.BLUE}")
    print(timestampStr)
    print(f"{bcolors.WHITE}")
    f.write(timestampStr)
    f.write("\n")

    print()

    # Print the keys and values of the dictionary
    for machine in machines:
        octets = machines[machine]['IP'].split('.')
        if octets[2] == "1":  # then it's 10.1
            pingString = "ping " + machines[machine]['IP'] + " -n 1"
            response = os.popen(pingString).read()
            # print (pingString)
            # print(response)

            if "Received = 1" in response and "Approximate" in response:
                print(f"{bcolors.CYAN} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") UP")
            else:
                print(f"{bcolors.RED} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") DOWN")
                f.write(machines[machine]['Location'] + " (" + machine + " " +  machines[machine]['IP'] + ") DOWN\n")

        if octets[2] == "66" or octets[2] == "65":  # then it's 192.168.66
            # Octavio's code
            node = pyeapi.connect(transport="https", host="192.168.68.1", username="admin", password="n51ght!", port=443)
            # res = node.execute(["ping 192.168.66.%s repeat 1" % machine])["result"][0]["messages"][0]
            res = node.execute(["ping %s repeat 1" % machines[machine]['IP']])["result"][0]["messages"][0]
            if "ttl" in res:
                print(f"{bcolors.CYAN} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") UP")
            else:
                print(f"{bcolors.RED} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") DOWN")
                f.write(machines[machine]['Location'] + " (" + machine + " " + machines[machine]['IP'] + ") DOWN\n")

        if octets[2] == "68":  # then it's 192.168.68
            # Octavio's code
            node = pyeapi.connect(transport="https", host="192.168.68.1", username="monitoring", password="monitoring", port=443)
            res = node.execute(["ping vrf EXTERNAL %s repeat 1" % machines[machine]['IP']])["result"][0]["messages"][0]
            if "ttl" in res:
                print(f"{bcolors.CYAN} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") UP")
            else:
                print(f"{bcolors.RED} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine][
                    'Location'] + ") DOWN")
                f.write(machines[machine]['Location'] + " (" + machine + " " + machines[machine]['IP'] + ") DOWN\n")

    time.sleep(300)