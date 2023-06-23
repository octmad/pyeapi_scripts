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

import os
import time
import pyeapi
from datetime import datetime

# Create a nested dictionary
machines={'Corp Net': {'Location': "Data Center", 'IP': "10.1.1.1", 'DeviceType': "switch"},
          'Corp 7280': {'Location': "Data Center", 'IP': "10.1.1.146", 'DeviceType': "switch"},
          'Corp 7020': {'Location': "Dmark", 'IP': "10.1.1.50", 'DeviceType': "switch"},		  
          'Lambda': {'Location': "Data Center", 'IP': "10.1.1.85", 'DeviceType': "computer"},
          'DGX': {'Location': "Data Center", 'IP': "10.1.1.48", 'DeviceType': "computer"},
          'Big Mac': {'Location': "Data Center", 'IP': "10.1.1.94", 'DeviceType': "computer"},
          'Xavier1': {'Location': "Data Center", 'IP': "10.1.1.102", 'DeviceType': "computer"},
          'Xavier2': {'Location': "Data Center", 'IP': "10.1.1.80", 'DeviceType': "computer"},
          'Xavier3': {'Location': "Data Center", 'IP': "10.1.1.72", 'DeviceType': "computer"},
          'Xavier4': {'Location': "Data Center", 'IP': "10.1.1.99", 'DeviceType': "computer"},
          'Orin1': {'Location': "Data Center", 'IP': "10.1.1.111", 'DeviceType': "computer"},
          'Orin2': {'Location': "Data Center", 'IP': "10.1.1.83", 'DeviceType': "computer"},
          'Emergent7280': {'Location': "Lab B", 'IP': "10.1.1.69", 'DeviceType': "switch"},
          'EmergentDev': {'Location': "Lab B", 'IP': "10.1.1.67", 'DeviceType': "computer"},
          'NDI_Dev': {'Location': "Lab B", 'IP': "10.1.1.56", 'DeviceType': "computer"},
          'FrankJump': {'Location': "Lab B", 'IP': "10.1.1.123", 'DeviceType': "computer"},
          'Jump1-Mirror': {'Location': "Lab B", 'IP': "10.1.1.86", 'DeviceType': "computer"},
          'PugetVid': {'Location': "Lab B", 'IP': "10.1.1.84", 'DeviceType': "computer"},
          'OmenLeft': {'Location': "Lab B", 'IP': "10.1.1.104", 'DeviceType': "computer"},
          'Emergent100': {'Location': "Lab B", 'IP': "192.168.66.100", 'DeviceType': "camera"},
          'Emergent101': {'Location': "Lab B", 'IP': "192.168.66.101", 'DeviceType': "camera"},		  
          'Emergent102': {'Location': "Lab B", 'IP': "192.168.66.102", 'DeviceType': "camera"},
          'Emergent103': {'Location': "Lab B", 'IP': "192.168.66.103", 'DeviceType': "camera"}}

while (1):
    os.system('cls' if os.name == 'nt' else 'clear')

    f=open("corpNet DownLog.txt", "a")

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
        if octets[2] == "1":	# then it's 10.1
            pingString = "ping " + machines[machine]['IP'] + " -n 1"
            response = os.popen(pingString).read()
            # print (pingString)
            # print(response)

            if "Received = 1" in response and "Approximate" in response:
                print(f"{bcolors.CYAN} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine]['Location'] + ") UP")
            else:
                print(f"{bcolors.RED} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine]['Location'] + ") DOWN")
                f.write(machines[machine]['Location'] + " (" + machine + " " + machines[machine]['IP'] + ") DOWN\n")
	
        if octets[2] == "66":	# then it's 192.168.66
            # Octavio's code
            node = pyeapi.connect(transport="https", host="10.1.1.69", username="monitoring", password="monitoring", port=443)
            node.transport._context.set_ciphers('DEFAULT')
            # res = node.execute(["ping 192.168.66.%s repeat 1" % machine])["result"][0]["messages"][0]
            res = node.execute(["ping %s repeat 1"%machines[machine]['IP']])["result"][0]["messages"][0]
            if "ttl" in res:
                print(f"{bcolors.CYAN} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine]['Location'] + ") UP")
            else:
                print(f"{bcolors.RED} " + machine + " " + machines[machine]['IP'] + " (" + machines[machine]['Location'] + ") DOWN")
                f.write(machines[machine]['Location'] + " (" + machine + " " + machines[machine]['IP'] + ") DOWN\n")

    time.sleep( 300 ) 
	
	