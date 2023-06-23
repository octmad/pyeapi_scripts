import pyeapi
import pprint

# Create a List of Switches
#switches = ["192.168.68.1", "192.168.68.11","192.168.68.12","192.168.68.13"]
switches=["10.1.1.69","10.1.1.148","10.1.1.58"]
for switch in switches:
    # Define API Connection String
    node = pyeapi.connect(transport="https", host=switch, username="admin", password="n51ght!", port=443)
    node.transport._context.set_ciphers('DEFAULT')

    # Execute the desired command
    version = node.execute(["show version"])

    # Print the desired Output
    print
    print ("*******************************************************")
    print (("Switch IP: %s") % switch)
    print (("Model Name: %s") % version["result"][0]["modelName"])
    print (("Serial Number: %s") % version["result"][0]["serialNumber"])
    print (("EOS Version: %s") % version["result"][0]["version"])
    print ("*******************************************************")
    print


