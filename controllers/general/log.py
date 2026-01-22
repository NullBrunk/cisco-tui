from controllers.baseController import baseController 
from views.colors import *
import questionary

class Log(baseController):
    def __init__(self, interact):
        self.interact = interact

    def show(self, output: str):
        output = "\n".join(output.split("Log Buffer (")[1].split("\n")[1:])
        print(output)
    
    def run(self):
        self.interact.send("terminal length 0")
        output = self.interact.send("sh log")
        self.show(output)
