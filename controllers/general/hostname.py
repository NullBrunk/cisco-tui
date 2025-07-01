from controllers.baseController import baseController
from views.colors import *
import questionary 

class Hostname(baseController):
    def __init__(self, interact):
        self.interact = interact

    def show_hostname(self):
        return self.interact.get_prompt()
        
    def run(self):
        super().run()
        
        print(f"Hostname is: {BOLD_YELLOW}{self.show_hostname()}{NOCOLOR}\n")
        
        new_hostname = questionary.text("Enter new hostname:").ask()

        if(not new_hostname): quit()

        self.interact.send(f"hostname {new_hostname}", True)



