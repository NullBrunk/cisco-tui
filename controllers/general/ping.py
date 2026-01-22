from controllers.baseController import baseController
from views.colors import * 

from sys import argv

class Ping(baseController):
    def __init__(self, interact):
        self.interact = interact

    def run(self):
        super().run()

        if(not len(argv) >= 5):
            print("Ca va pas le faire")
            quit()

        res = self.interact.send(f"ping {argv[4]} repeat 1 timeout 1")

        split = res.split("\n")
        for i in range(len(res)):
            if "Sending" in split[i]:
                break

        string = "\n".join(split[i:])

        string = string.replace(argv[4], f"{BOLD_CYAN}{argv[4]}{NOCOLOR}")
        string = string.replace("100 percent (1/1)", f"{BOLD_GREEN}100 percent (1/1){NOCOLOR}")
        string = string.replace("0 percent (0/1)", f"{BOLD_YELLOW}0 percent (0/1){NOCOLOR}")

        print(string)
        


