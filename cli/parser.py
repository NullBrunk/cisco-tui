from cli.helper import helper, error
from sys import argv

def parse():
    if(len(argv) <= 2):
        helper(argv[0])
        quit()

    for arg in argv:
        if arg in ["--help", "-h"]:
            helper(argv[0])
            quit()

    ip = argv[0]
    port = argv[0]

    try:
        port = int(port)
    except ValueError:
        error(argv[0], "PORT must be an integer")
        quit()

    if(not (1 <= port <= 65535)):
        error(argv[0], "PORT must be an integer between 1 and 65535")
        quit()

    return ip, port