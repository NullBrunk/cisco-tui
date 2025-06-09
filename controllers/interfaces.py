from controllers.interact import Interact
from views.colors import *

import questionary
import ipaddress

class Interfaces:
    def __init__(self, connection):
        self.interact = Interact(connection)

        self.INTERFACES = {}
        self.INTERFACE = None

        self.gather_interfaces()

    def gather_interfaces(self):
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

    def show_interface(self):
        result = self.interact.send(f"sh ip int {self.INTERFACE}").split("\n")

        line1 = result[0].strip().replace("administratively down", f"{BOLD_YELLOW}administratively down{NULL}")
        line1 = line1.strip().replace("down", f"{BOLD_YELLOW}down{NULL}")
        line1 = line1.strip().replace("up", f"{BOLD_GREEN}up{NULL}")

        line2 = result[1].strip()
        line2 = line2.strip().replace("disabled", f"{BOLD_RED}disabled{NULL}")

        if("address is " in line2):
            line2 = line2.split("is")
            line2 = f"{line2[0]}is{BOLD_CYAN}{line2[1]}"

        print(f"\n{line1}\n{line2}\n")

    def get_interface(self):
        cmd = questionary.select(
            "Which interface do you want to configure?",
            choices=[
                *self.INTERFACES,
                "Enter manually",
        ]).ask()

        interface = None

        if(cmd == "Enter manually"):
            interface = questionary.text("Enter custom interface (e.g. Lo0):").ask()
        else:
            interface = cmd

        return interface


    def ip_config(self):
        cidr = questionary.text("Enter IP address (e.g. 10.0.0.254/24) ").ask()
        net = ipaddress.IPv4Network(cidr, strict=False)

        config = f"""int {self.INTERFACE}
                     ip address {cidr.split("/")[0]} {net.netmask}
                     no sh
                """

        self.interact.send(config, True)

    def run(self):
        
        self.INTERFACE = self.get_interface()
        self.show_interface()

        cmd = questionary.select(
            "What do you want to do?",
            choices=[
               "Configure an IP",
               "Up the interface",
               "Down the interface",
               "Exit",
        ]).ask()

        match cmd:
            case "Configure an IP":
                self.ip_config()

            case "Up the interface":
                print("INTERFACE UP")
            case "Down the interface":
                print("INT DOWN")
            case "Exit":
                quit()

        quit()



