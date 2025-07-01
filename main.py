#!/usr/bin/env python3

from controllers.general.hostname import Hostname
from controllers.general.save import Save
from controllers.general.show import Show

from controllers.interfaces.ipv4 import Ipv4
from controllers.interfaces.down import Down
from controllers.interfaces.up import Up

from services.getInterfaces import getInterfaces
from services.interact import Interact

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
    controller = None

    if "ipv4".startswith(command.lower()):
        controller = Ipv4(interact, getInterfaces(interact))

    elif "down".startswith(command.lower()):
        controller = Down(interact, getInterfaces(interact))

    elif "up".startswith(command.lower()):
        controller = Up(interact, getInterfaces(interact))

    elif "hostname".startswith(command.lower()):
        controller = Hostname(interact)

    elif "show".startswith(command.lower()):
        controller = Show(interact)

    elif "save".startswith(command.lower()):
        controller = Save(interact)

    elif "static".startswith(command.lower()):
        controller = Static(interact)

    elif "ospf".startswith(command.lower()):
        controller = Ospf(interact)

    elif "bgp".startswith(command.lower()):
        controller = Bgp(interact)

    else:
        error(program_name, f"Unrecognized command {command}")
        quit()

    controller.run()

if __name__ == "__main__":
    main()