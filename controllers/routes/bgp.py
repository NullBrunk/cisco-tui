from controllers.baseController import baseController

class Bgp(baseController):
    def __init__(self, interact):
        self.interact = interact

    def run(self):
        super().run()
