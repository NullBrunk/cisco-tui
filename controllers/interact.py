class Interact:
    def __init__(self, session):
        self.session = session

    def send(self, command: str, config: bool = False):
        if(config):
            command = command.split("\n")
            for i in range(len(command)):
                command[i] = command[i].strip()
                
                if(command[i] == ""):
                    del command[i]

            return self.session.send_config_set(command)

        return self.session.send_command(command)
