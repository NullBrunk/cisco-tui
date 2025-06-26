from controllers.interact import Interact
from views.colors import *

import questionary
import ipaddress

class Interfaces:
    def __init__(self, interact):
        self.interact = interact
        self.INTERFACES = {}
    
        self.get_interfaces()
       

    # Gather all interfaces an store them in a dict
    def get_interfaces(self) -> dict:
        output = self.interact.send("show ip interface brief")
        # Get rid of header (Interface                  IP-Address      OK? Method Status                Protocol)
        output = output.split("\n")[1:]

        for interface_line in output:
            interface = interface_line.split()
            
            if(len(interface) < 5):
                continue

            self.INTERFACES[interface[0]] = {
                "ip": interface[1],
                "status": interface[4] if interface[4] != "administratively" else "administratively down",
            }


    def show_interfaces(self):
        for key in self.INTERFACES:
            print(self.INTERFACES[key])

   