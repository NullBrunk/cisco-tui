from controllers.interface import Interface
from views.colors import *
import questionary

class Up:
    def __init__(self, interact, INTERFACES):
        self.interact = interact
        self.INTERFACES = INTERFACES

    def gather_interfaces(self):
        inames = questionary.checkbox(
            "Which interface do you want to up?",
            choices=[
                *self.INTERFACES,
        ], qmark="?", instruction=" ").ask()

        return inames

    def run(self):
        inames = self.gather_interfaces()

        for iname in inames:
            interface = Interface(iname, self.interact)

            print(f"\n{BOLD_BLUE}>{BOLD_WHITE} Upping {BOLD_BLUE}{iname}{NOCOLOR}")
            output = interface.up()
            
            show = False
            for line in output.split("\n"):
                if("int" in line):
                    show = True
                if(show):
                    print(line)
                if("sh" in line):
                    show = False