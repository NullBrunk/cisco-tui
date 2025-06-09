from views.colors import *

def help_menu(program_name: str):
    print(f"""{WHITE}TUI tool to simplify Cisco IOS configuration

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} <IP> <PORT> <COMMAND>

{BOLD_GREEN}Options:
  {BOLD_CYAN}IP              {NULL}{WHITE}The Cisco IOS Telnet IP
  {BOLD_CYAN}PORT            {NULL}{WHITE}The Cisco IOS Telnet port

{BOLD_GREEN}Commands:
  {BOLD_CYAN}interfaces      {NULL}{WHITE}Configure interfaces
""")

def interfaces_help_menu(program_name: str):
    print(f"""{WHITE}Configure interfaces

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} <IP> <PORT> interfaces (OPTIONS)

{BOLD_GREEN}Options:
  {BOLD_CYAN}tui (default)     {NULL}{WHITE}Configure interfaces in TUI mode
  {BOLD_CYAN}show              {NULL}{WHITE}Show all the interfaces
""")

def missing_mandatory(argv: list):
    missing = None
    missing_arg = None

    if(len(argv) == 2):
        missing_arg = "PORT"
    elif(len(argv) == 3):
        missing_arg = "COMMAND"

    print(f"""{BOLD_RED}error: {NULL}{WHITE}the following required arguments were not provided:
  {BOLD_CYAN}<{missing_arg}>

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> <COMMAND>

{NULL}{WHITE}For more information, try '{BOLD_CYAN}--help{NULL}{WHITE}'.
""")


def error(program_name: str, msg: str):
    print(f"""{BOLD_RED}error: {NULL}{WHITE}{msg}

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} <IP> <PORT>

{WHITE}For more information, try '{BOLD_CYAN}--help{NULL}{WHITE}'.
""")