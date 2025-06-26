#!/usr/bin/env python3

from controllers.interact import Interact
from controllers.hostname import Hostname
from controllers.ipv4 import Ipv4
from controllers.down import Down
from controllers.show import Show
from controllers.up import Up
from models.interfaces import Interfaces

from cli.parser import parse
from cli.cli import *

from netmiko import ConnectHandler 


def main():
    program_name, ip, port, command, non_mandatory = parse()

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
            interfaces_help_menu(program_name)

    elif "down".startswith(command.lower()):
            down = Down(interact, INTERFACES)
            
            if(non_mandatory == None or non_mandatory == "tui"):
                down.run()

            if(non_mandatory == "--help" or non_mandatory == "-h"):
                down_help_menu(program_name)

    elif "up".startswith(command.lower()):
        up = Up(interact, INTERFACES)
        
        if(non_mandatory == None or non_mandatory == "tui"):
            up.run()

        if(non_mandatory == "--help" or non_mandatory == "-h"):
            up_help_menu(program_name)

    elif "hostname".startswith(command.lower()):
        hostname = Hostname(interact)

        if(non_mandatory == None or non_mandatory == "tui"):
            hostname.run()
        
        if(non_mandatory == "--help" or non_mandatory == "-h"):
            hostname_help_menu(program_name)

    elif "show".startswith(command.lower()):
        show = Show(interact, INTERFACES)

        if(non_mandatory == None or non_mandatory == "tui"):
            show.run()

        if(non_mandatory == "--help" or non_mandatory == "-h"):
            show_help_menu(program_name)

    else:
        error(program_name, f"Unrecognized command {command}")
        

if __name__ == "__main__":
    main()