#!/usr/bin/env python3

from services.getInterfaces import getInterfaces
from services.interact import Interact

from controllers.general.hostname import Hostname
from controllers.general.reload import Reload
from controllers.general.save import Save
from controllers.general.show import Show
from controllers.general.ping import Ping
from controllers.general.exec import Exec
from controllers.general.log import Log

from controllers.interfaces.ipv4 import Ipv4
from controllers.interfaces.down import Down
from controllers.interfaces.up import Up

from controllers.routes.static import Static
from controllers.routes.ospf import Ospf
from controllers.routes.bgp import Bgp

from cli.parser import parse
from cli.cli import *

from netmiko import ConnectHandler 

def main():
    program_name, ip, port, general_command, command = parse()

    net_connect = ConnectHandler(
        device_type="cisco_ios_telnet",
        host=ip,
        port=port,
        fast_cli=True,
    )

    interact = Interact(net_connect)
    interact.enable()
    
    controller = None

    if(general_command in ["interface", "i"]):
        if "ipv4".startswith(command.lower()):
            controller = Ipv4(interact, getInterfaces(interact))

        elif "down".startswith(command.lower()):
            controller = Down(interact, getInterfaces(interact))

        elif "up".startswith(command.lower()):
            controller = Up(interact, getInterfaces(interact))

        else:
            error(f"Unrecognized command {command}")

    
    elif(general_command in ["global", "g"]):
        if "hostname".startswith(command.lower()):
            controller = Hostname(interact)

        elif "ping".startswith(command.lower()):
            controller = Ping(interact)

        elif "show".startswith(command.lower()):
            controller = Show(interact)

        elif "save".startswith(command.lower()):
            controller = Save(interact)

        elif "exec".startswith(command.lower()):
            if(not non_mandatory):
                error("Missing the command to execute")
                quit()
                
            controller = Exec(interact, non_mandatory)

        elif "reload".startswith(command.lower()):
            controller = Reload(interact)

        elif "log".startswith(command.lower()):
            controller = Log(interact)

        else:
            error(f"Unrecognized command {command}")

    
    elif(general_command in ["routing", "r"]):
        if "static".startswith(command.lower()):
            controller = Static(interact)

        elif "ospf".startswith(command.lower()):
            controller = Ospf(interact)

        elif "bgp".startswith(command.lower()):
            controller = Bgp(interact)

        else:
            error(f"Unrecognized command {command}")

    
    else:
        error(f"Unrecognized command {command}")

    controller.run()

if __name__ == "__main__":
    main()
