from cli.cli import *
from sys import argv

def argv_exists(index: int):
    return len(argv) > index

def is_help(index: int):
    if(argv_exists(index)):
        return argv[index] in ["help", "h", "--help", "-h"]

    quit()

def is_command(index: int):
    if(argv_exists(index)):
        return argv[index] in ["general", "g", "interface", "i", "routing", "r"]

    quit()

def validate_port(port: int):
    try:
        port = int(port)
    except ValueError:
        error("PORT must be an integer")
        quit()

    if(not (1 <= port <= 65535)):
        error("PORT must be an integer between 1 and 65535")
        quit()

    return port

def modulable_help_menu(arg: int):
    if(is_command(arg)):
        if(argv[arg] in ["general", "g"]):
            help_general()
        elif(argv[arg] in ["interface", "i"]):
            help_interface()
        elif(argv[arg] in ["routing", "r"]):
            help_routing()

def parse():
    ip = None
    port = None
    command = None
    argument = None
    #commands = ["general", "g", "interface", "i", "routing", "r"]

    if(not argv_exists(1) or is_help(1)):
        help_menu()

    modulable_help_menu(1)


    if(argv_exists(1) and argv_exists(2)):
        ip = argv[1]
        port = validate_port(argv[2])
    else:
        help_menu()

    #ici on a ip et port de set
    if(argv_exists(3) and is_command(3)):
        command = argv[3]
    else:
        help_menu()

    if(not argv_exists(4) or is_help(4)):
        modulable_help_menu(3)

    argument = argv[4]

    return argv[0], ip, port, command, argument

