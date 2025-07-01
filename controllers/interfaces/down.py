from controllers.baseController import baseController
from models.interface import Interface
from views.colors import *
import questionary

class Down(baseController):
    def __init__(self, interact, INTERFACES):
        self.interact = interact
        self.INTERFACES = INTERFACES

    def gather_interfaces(self):
        inames = questionary.checkbox(
            "Which interface do you want to down?",
            choices=[
                *self.INTERFACES,
        ], qmark="?", instruction=" ").ask()

        return inames

    def run(self):
        super().run()

        inames = self.gather_interfaces()

        for iname in inames:
            interface = Interface(iname, self.interact)

            print(f"\n{BOLD_WHITE}❯{BOLD_RED} Shutting down {BOLD_WHITE}{iname}{NOCOLOR}")
            output = interface.down()
            
            show = False
            for line in output.split("\n"):
                if("int" in line):
                    show = True
                if(show):
                    print(line)
                if("no sh" in line):
                    show = False