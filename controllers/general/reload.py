from controllers.baseController import baseController 
from views.colors import *
import questionary
import netmiko

class Reload(baseController):
    def __init__(self, interact):
        self.interact = interact

    def run(self):
        print(f"{BOLD_CYAN}Reloading ...{NOCOLOR}")
        try:
            self.interact.send("reload\nyes\n")
        except netmiko.exceptions.ReadTimeout:
            pass

        logs = None
        while True:
            try:
                self.interact.enable()
                self.interact.send("terminal length 0")
                logs = self.interact.send("sh log")
            except netmiko.exceptions.ReadTimeout:
                pass

            if(not logs):
                continue

            break

        print(f"{BOLD_CYAN}Done ...{NOCOLOR}")