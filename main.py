#!/usr/bin/env python3

from cli.cli import interfaces_help_menu
from cli.parser import parse

from netmiko import ConnectHandler 

from controllers.interfaces import Interfaces

def main():
    ip, port, command, non_mandatory = parse()

    net_connect = ConnectHandler(
        device_type="cisco_ios_telnet",
        host=ip,
        port=port,
        fast_cli=True,
    )
    net_connect.enable()
    

    if "interfaces".startswith(command.lower()):
        ic = Interfaces(net_connect)
        if(non_mandatory == None or non_mandatory == "tui"):
            ic.run()

        if(non_mandatory == "--help" or non_mandatory == "-h"):
            interfaces_help_menu()

        if(non_mandatory == "sh" or non_mandatory == "show"):
            ic.show_interfaces()


if __name__ == "__main__":
    main()