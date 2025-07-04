from controllers.baseController import baseController 
import questionary

class Exec(baseController):
    def __init__(self, interact, command: str):
        self.interact = interact
        self.command = command

    def show(self, output: str):
        print(output)

    def run(self):
        self.show(self.interact.send(self.command))