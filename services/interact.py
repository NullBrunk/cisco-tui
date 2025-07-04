class Interact:
    def __init__(self, session):
        self.session = session

    def enable(self):
        self.session.enable()

    def send(self, command: str, config: bool = False):
        if(config):
            command = command.split("\n")
            for i in range(len(command)):
                command[i] = command[i].strip()
                
                if(command[i] == ""):
                    del command[i]
            
            command.append("end")
            return self.session.send_config_set(command)

        return self.session.send_command(command)


    def get_prompt(self) -> str:
        send_command = self.send("no", True)
        send_command = send_command.split("\n")[-1].replace("#", "").replace(">", "")

        return send_command