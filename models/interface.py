from services.interact import Interact
from views.colors import *

class Interface:
    def __init__(self, iname, interact):
        self.interact = interact
        self.iname = iname

        self.state = None
        self.cidr = None

        self.populate()
        
    def populate(self):
        result = self.interact.send(f"sh ip int {self.iname}")
        
        if("address is " in result):
            self.cidr = result.split("address is ")[1].split(" ")[0]

        if("down" in result.lower()):
            self.state = False
        else:
            self.state = True      

    ### UTILITIES
    def set_ip(self, cidr, ip, netmask):
        self.cidr = cidr

        config = f"""int {self.iname}
                     ip address {ip} {netmask}
                     no sh
                """
        self.state = True
        return self.interact.send(config, config=True)

    def down(self):
        config = f"""int {self.iname}
                     sh
                """
        self.state = False
        return self.interact.send(config, config=True)

    def up(self):
        config = f"""int {self.iname}
                     no sh
                """
        self.state = True
        return self.interact.send(config, config=True)
    # ### END UTILITIES



    # def execute_command(self):
    #     cmd = questionary.select(
    #         "What do you want to do?",
    #         choices=[
    #            "Configure IP",
    #            "Down" if self.STATE else "Up",
    #            "Show",
    #            "Exit",
    #     ], qmark="?", instruction=" ").ask()

    #     match cmd:
    #         case "Configure an IP":
    #             self.ip_config()

    #         case "Up the interface":
    #             print("INTERFACE UP")
    #         case "Down the interface":
    #             print("INT DOWN")
    #         case "Show":
    #             self.show_interface()
    #         case "Exit":
    #             quit()

    # def run(self):
        
    #     self.INTERFACE = self.get_interface()

    #     self.show_interface()
        
    #     while True:
    #         self.execute_command()
            
    #     quit()


    # def harvest(self):
    #     

    #     line1 = result[0].strip().replace("administratively down", f"{BOLD_YELLOW}administratively down{NOCOLOR}")
    #     line1 = line1.strip().replace("down", f"{BOLD_YELLOW}down{NOCOLOR}")
    #     line1 = line1.strip().replace("up", f"{BOLD_GREEN}up{NOCOLOR}")

    #     line2 = result[1].strip()
    #     line2 = line2.strip().replace("disabled", f"{BOLD_RED}disabled{NOCOLOR}")
