#!/usr/bin/env python3

from controllers.interfaces import Interfaces
from controllers.interact import Interact
from controllers.ipv4 import Ipv4
from controllers.down import Down
from controllers.up import Up

from cli.cli import interfaces_help_menu
from cli.parser import parse

from netmiko import ConnectHandler 


def main():
    ip, port, command, non_mandatory = parse()

    net_connect = ConnectHandler(
        device_type="cisco_ios_telnet",
        host=ip,
        port=port,
        fast_cli=True,
    )
    net_connect.enable()
    interact = Interact(net_connect)

    interfacesController = Interfaces(interact)
    INTERFACES = interfacesController.INTERFACES

    if "ipv4".startswith(command.lower()):
        ipv4 = Ipv4(interact, INTERFACES)
        
        if(non_mandatory == None or non_mandatory == "tui"):
            ipv4.run()

        if(non_mandatory == "--help" or non_mandatory == "-h"):
            interfaces_help_menu()

    elif "down".startswith(command.lower()):
            down = Down(interact, INTERFACES)
            
            if(non_mandatory == None or non_mandatory == "tui"):
                down.run()

            if(non_mandatory == "--help" or non_mandatory == "-h"):
                down_help_menu()

    elif "up".startswith(command.lower()):
        up = Up(interact, INTERFACES)
        
        if(non_mandatory == None or non_mandatory == "tui"):
            up.run()

        if(non_mandatory == "--help" or non_mandatory == "-h"):
            up_help_menu()

if __name__ == "__main__":
    main()