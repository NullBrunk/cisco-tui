from services.interact import Interact
import ipaddress

def getInterfaces(interact):
    INTERFACES = {}
    
    output = interact.send("show ip interface brief")
    # Get rid of header (Interface                  IP-Address      OK? Method Status                Protocol)
    output = output.split("\n")[1:]

    for interface_line in output:
        interface = interface_line.split()
        
        if(len(interface) < 5):
            continue

        INTERFACES[interface[0]] = {
            "ip": interface[1],
            "status": interface[4] if interface[4] != "administratively" else "administratively down",
        }

    return INTERFACES