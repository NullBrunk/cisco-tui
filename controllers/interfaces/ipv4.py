from controllers.baseController import baseController
from models.interface import Interface
from views.colors import *
import questionary
import ipaddress

class Ipv4(baseController):
    def __init__(self, interact, INTERFACES):
        self.interact = interact
        self.INTERFACES = INTERFACES

        self.interface = None


    def gather_interface(self):
        iname = questionary.select(
            "Which interface do you want to configure?",
            choices=[
                *self.INTERFACES,
                "Enter manually",  
        ], qmark="?", instruction=" ").ask()

        if(iname == "Enter manually"):
            iname = questionary.text("Enter custom interface (e.g. Lo0):").ask()

        if(not iname): quit()
        
        return iname


    def ip_config(self):
        cidr = questionary.text("IP address (e.g 10.0.0.1/24):").ask()

        if(not cidr): quit()


        net = ipaddress.IPv4Network(cidr, strict=False)
        ip = cidr.split("/")[0]

        return self.interface.set_ip(cidr, ip, net.netmask)


    ### Configure an IP on a specific interface
    def run(self):
        super().run()

        iname = self.gather_interface()
        self.interface = Interface(iname, self.interact)

        print(f"\nCurrent IP is: {BOLD_YELLOW}{self.interface.cidr}{NOCOLOR}")
        
        output = self.ip_config()

        show = False
        for line in output.split("\n"):
            if("int" in line):
                show = True
            if(show):
                print(line)
            if("no sh" in line):
                show = False
