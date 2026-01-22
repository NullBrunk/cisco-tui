from views.colors import *
from sys import argv

def help_menu():
    print(f"""{WHITE}TUI tool to simplify Cisco IOS configuration

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> <COMMAND> [ARGUMENT]

{BOLD_GREEN}OPTIONS:
    {BOLD_CYAN}IP                          {NOCOLOR}{WHITE}The Cisco IOS Telnet IP
    {BOLD_CYAN}PORT                        {NOCOLOR}{WHITE}The Cisco IOS Telnet port

{BOLD_GREEN}COMMANDS:
    {BOLD_CYAN}general{BOLD_WHITE}, {BOLD_CYAN}g                  {NOCOLOR}{WHITE}Configure system
    {BOLD_CYAN}interface{BOLD_WHITE}, {BOLD_CYAN}i                {NOCOLOR}{WHITE}Configure interface
    {BOLD_CYAN}routing{BOLD_WHITE}, {BOLD_CYAN}r                  {NOCOLOR}{WHITE}Configure routing""")
    quit()


def help_general():
    print(f"""{WHITE}Configure system

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> general [ARGUMENT]

{BOLD_GREEN}ARGUMENTS:
    {BOLD_CYAN}hostname         {NOCOLOR}{WHITE}Get/set the router hostname
    {BOLD_CYAN}reload           {NOCOLOR}{WHITE}Reboot the router
    {BOLD_CYAN}ping             {NOCOLOR}{WHITE}Send ICMP echo request
    {BOLD_CYAN}show             {NOCOLOR}{WHITE}Get informations (sh commands)
    {BOLD_CYAN}save             {NOCOLOR}{WHITE}Write the running config  
    {BOLD_CYAN}log              {NOCOLOR}{WHITE}Show logs""")
    quit()


def help_interface():
    print(f"""{WHITE}Configure interface
{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> interface [ARGUMENT]

{BOLD_GREEN}ARGUMENTS:
    {BOLD_CYAN}ipv4             {NOCOLOR}{WHITE}Configure IPv4 on an interface
    {BOLD_CYAN}down             {NOCOLOR}{WHITE}Down a group of interface
    {BOLD_CYAN}up               {NOCOLOR}{WHITE}Up a group of interface""")
    quit()


def help_routing():
    print(f"""{WHITE}Configure routing
{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> routing [ARGUMENT]

{BOLD_GREEN}ARGUMENTS:
  {BOLD_CYAN}static           {NOCOLOR}{WHITE}Configure static routes
  {BOLD_CYAN}ospf             {NOCOLOR}{WHITE}Configure ospf routing
  {BOLD_CYAN}bgp              {NOCOLOR}{WHITE}Configure bgp routing
""")
    quit()


def missing_mandatory(argv: list):
    missing = None
    missing_arg = None

    if(len(argv) == 2):
        missing_arg = "PORT"
    elif(len(argv) == 3):
        missing_arg = "COMMAND"

    print(f"""{BOLD_RED}error: {NOCOLOR}{WHITE}the following required arguments were not provided:
  {BOLD_CYAN}<{missing_arg}>

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> <COMMAND> [ARGUMENT]

{NOCOLOR}{WHITE}For more information, try '{BOLD_CYAN}--help{NOCOLOR}{WHITE}'.
""")

def error(msg: str):
    print(f"""{BOLD_RED}error: {NOCOLOR}{WHITE}{msg}

{BOLD_GREEN}Usage: {BOLD_CYAN}{argv[0]} <IP> <PORT> <COMMAND> [ARGUMENT]

{WHITE}For more information, try '{BOLD_CYAN}--help{NOCOLOR}{WHITE}'.
""")
    quit()
