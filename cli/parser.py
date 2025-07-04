from cli.cli import help_menu, error, missing_mandatory
from sys import argv

def parse():
    for arg in argv[:4]:
        if arg in ["--help", "-h"]:
            help_menu(argv[0])
            quit()

    if(len(argv) <= 3):
        help_menu(argv[0])
        quit()

   
    ip = argv[1]
    port = argv[2]
    command = argv[3]
    

    try:
        port = int(port)
    except ValueError:
        error(argv[0], "PORT must be an integer")
        quit()

    if(not (1 <= port <= 65535)):
        error(argv[0], "PORT must be an integer between 1 and 65535")
        quit()

    if(len(argv) > 4):
        return argv[0], ip, port, command, ' '.join(argv[4:])

    return argv[0], ip, port, command, None