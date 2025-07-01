from views.colors import *

def help_menu(program_name: str):
    print(f"""{WHITE}TUI tool to simplify Cisco IOS configuration

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} <IP> <PORT> <COMMAND>

{BOLD_GREEN}OPTIONS:
  {BOLD_CYAN}IP               {NOCOLOR}{WHITE}The Cisco IOS Telnet IP
  {BOLD_CYAN}PORT             {NOCOLOR}{WHITE}The Cisco IOS Telnet port

{BOLD_GREEN}COMMANDS:
  {BOLD_CYAN}hostname         {NOCOLOR}{WHITE}Get/set the router hostname
  {BOLD_CYAN}show             {NOCOLOR}{WHITE}Get informations (sh commands)
  {BOLD_CYAN}save             {NOCOLOR}{WHITE}Write the running config  

  {BOLD_CYAN}ipv4             {NOCOLOR}{WHITE}Configure IPv4 on an interface
  {BOLD_CYAN}down             {NOCOLOR}{WHITE}Down a group of interface
  {BOLD_CYAN}up               {NOCOLOR}{WHITE}Up a group of interface

  {BOLD_CYAN}static           {NOCOLOR}{WHITE}Configure static routes
  {BOLD_CYAN}ospf             {NOCOLOR}{WHITE}Configure ospf routing
  {BOLD_CYAN}bgp              {NOCOLOR}{WHITE}Configure ospf routing
""")


def missing_mandatory(argv: list):
    missing = None
    missing_arg = None

    if(len(argv) == 2):
        missing_arg = "PORT"
    elif(len(argv) == 3):
        missing_arg = "COMMAND"

    print(f"""{BOLD_RED}error: {NOCOLOR}{WHITE}the following required arguments were not provided:
  {BOLD_CYAN}<{missing_arg}>

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> <COMMAND>

{NOCOLOR}{WHITE}For more information, try '{BOLD_CYAN}--help{NOCOLOR}{WHITE}'.
""")

def error(program_name: str, msg: str):
    print(f"""{BOLD_RED}error: {NOCOLOR}{WHITE}{msg}

{BOLD_GREEN}Usage: {BOLD_CYAN}{program_name} <IP> <PORT> <COMMAND>

{WHITE}For more information, try '{BOLD_CYAN}--help{NOCOLOR}{WHITE}'.
""")