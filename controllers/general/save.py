from controllers.baseController import baseController

class Save(baseController):
    def __init__(self, interact):
        self.interact = interact

    def run(self):
        super().run()

        print("\n".join(self.interact.send("wr").split("\n")[:3]))
