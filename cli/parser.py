from cli.cli import help_menu, error
from sys import argv

def parse():
    if(len(argv) <= 2):
        help_menu(argv[0])
        quit()

    for arg in argv:
        if arg in ["--help", "-h"]:
            help_menu(argv[0])
            quit()

    ip = argv[1]
    port = argv[2]

    try:
        port = int(port)
    except ValueError:
        error(argv[0], "PORT must be an integer")
        quit()

    if(not (1 <= port <= 65535)):
        error(argv[0], "PORT must be an integer between 1 and 65535")
        quit()

    return ip, port