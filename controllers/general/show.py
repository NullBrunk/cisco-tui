from controllers.baseController import baseController
from views.colors import *
from re import search
import questionary

class Show(baseController):
    def __init__(self, interact):
        self.interact = interact

    def show_ipv4(self):
        print()
        #                                        Get rid of the first and last line
        sh = self.interact.send("sh ip int br").split("\n")[1:-1]
        to_show = ""

        for line in sh:
            line = line.split()

            if(len(line) == 7):
                line[4] = line[4] + " " + line[5]
                del line[5]

            iname, ip, ok, method, status, protocol = line

            space_after_iname = 25 - len(iname)
            space_after_ip = 17 - len(ip)
            space_after_method = 7 - len(method) 
            space_after_status = 23 - len(status)


            string = f"{BLUE}{iname}{space_after_iname * ' '}"
            
            if("unassigned" in ip):
                string += f"{NOCOLOR}{ip}{space_after_ip * ' '}"
            else:
                string += f"{NOCOLOR}{CYAN}{ip}{space_after_ip * ' '}"
            
            if("unset" in method):
                string += f"{NOCOLOR}{method}{space_after_method * ' '}"
            else:
                string += f"{NOCOLOR}{CYAN}{method}{space_after_method * ' '}"
            
            if("down" in status):
                string += f"{NOCOLOR}{RED}{status}"
            else:
                string += f"{NOCOLOR}{GREEN}{status}"

            to_show += f"{string}\n"

        menu = f"{BOLD_WHITE}Interface" + (25 - len(iname) - (len("Interface") - len(iname)) ) * " "
        menu += "IP-Address" + (17 - len(ip) - (len("IP-Address") - len(ip)) ) * " "
        menu += "Method" + (7 - len(method) - (len("Method") - len(method)) ) * " "
        menu += f"Status{NOCOLOR}" 

        print(menu)
        print(to_show, end="")


    def show_route(self):
        sh = self.interact.send("sh ip route")
        print(sh)
    
    def show_version(self):
        sh = self.interact.send("sh version")
        
        print()

        for line in sh.split("\n"):
            if(
                search("IOS", line) 
                or search("Compiled", line) 
                or search("System", line) 
                or search("processor", line) 
                or search("board", line) 
                or search("interfaces", line) 
                or search("NVRAM", line) 
            ):
                print(line) 
                 
            elif(search("ROM", line) or search("uptime", line) or search("Last", line)):
                print(line + "\n") 

    def run(self):
        super().run()

        command = questionary.select(
            "What do you want to do?",
            choices=[
                "ipv4", 
                "route", 
                "version"
        ], qmark="?", instruction=" ").ask()

        if(not command): quit()
        
        if command == "ipv4": self.show_ipv4()
        elif command == "route": self.show_route()
        elif command == "version": self.show_version()
