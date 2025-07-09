from controllers.baseController import baseController
from models.interface import Interface
from views.colors import *
import questionary

class Up(baseController):
    def __init__(self, interact, INTERFACES):
        quit()
        self.interact = interact
        self.INTERFACES = INTERFACES

    def gather_interfaces(self):
        inames = questionary.checkbox(
            "Which interface do you want to up?",
            choices=[
                *self.INTERFACES,
        ], qmark="?", instruction=" ").ask()

        if(not inames or inames == []): quit()

        return inames

    def run(self):
        super().run()

        inames = self.gather_interfaces()

        for iname in inames:
            interface = Interface(iname, self.interact)

            print(f"\n{BOLD_WHITE}❯{BOLD_GREEN} Upping {BOLD_WHITE}{iname}{NOCOLOR}")
            output = interface.up()
            
            show = False
            for line in output.split("\n"):
                if("int" in line):
                    show = True
                if(show):
                    print(line)
                if("sh" in line):
                    show = False