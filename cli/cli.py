from views.colors import *

def help_menu(program_name: str):

    print(f"""{WHITE}TUI tool to simplify Cisco IOS configuration

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} [IP] [PORT]

{BOLD_GREEN}Options:
  {BOLD_CYAN}IP            {NULL}{WHITE}The Cisco IOS Telnet IP
  {BOLD_CYAN}PORT          {NULL}{WHITE}The Cisco IOS Telnet port
""")

def error(program_name: str, msg: str):
    print(f"""{BOLD_RED}error: {NULL}{WHITE}{msg}

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} [IP] [PORT]

{WHITE}For more information, try '{BOLD_CYAN}--help{NULL}{WHITE}'.
""")