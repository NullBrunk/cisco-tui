from controllers.baseController import baseController
from views.colors import * 
import questionary
import ipaddress

class Static(baseController):
    def __init__(self, interact):
        self.interact = interact
        self.route = None
        self.next_hop = None

        self.remote_network = None
        self.remote_mask = None

    def check(self):
        ret = self.interact.send(f"ping {self.next_hop} repeat 1")

        if("Success rate is 0 percent" in ret):
            print(f"\n{BOLD_RED}WARNING: {NOCOLOR}{WHITE}{self.next_hop} appears to be unreachable")
            
            if(not questionary.confirm("The ping test failed. Do you want to continue anyway? ").ask()):
                quit()
            

    def make_route(self):
        self.remote_network, self.remote_mask = self.parse_route()
        self.check()

        config = f"""ip route {self.remote_network} {self.remote_mask} {self.next_hop}"""
        return self.interact.send(config, True)


    def parse_route(self):
        parsed = ipaddress.IPv4Network(self.route, strict=False)
        
        remote_network = parsed.network_address
        remote_mask = parsed.netmask

        return remote_network, remote_mask


    def show(self, res: str):
        split = res.split("\n")

        for i in range(len(split)):
            if("ip" in split[i]):
                break
            
        print()
        to_show = "\n".join(split[i:-1])
        
        to_show = to_show.replace(f"{self.remote_network}", f"{BOLD_CYAN}{self.remote_network}")
        to_show = to_show.replace(f"{self.remote_mask}", f"{BOLD_CYAN}{self.remote_mask}")
        to_show = to_show.replace(f"{self.next_hop}", f"{BOLD_BLUE}{self.next_hop}{NOCOLOR}")

        print(to_show)


    def run(self):
        super().run()

        self.route = questionary.text("Destination network (e.g 192.168.0.0/24) ?").ask()
        self.next_hop = questionary.text("Next router (e.g 10.1.1.1) ?").ask()

        if(not self.route or not self.next_hop): quit()

        res = self.make_route()
        self.show(res) 



