from controllers.baseController import baseController 
import questionary
import ipaddress

class Ospf(baseController):
    def __init__(self, interact):
        self.interact = interact
        self.networks = {}

    def gather_networks(self):
        raw_networks = self.interact.send("sh run | include ip address").split("\n")
        
        for line in raw_networks:
            if not "ip address" in line or "no" in line:
                continue

            ip, mask = line.split("address ")[1].split(" ")            
            net = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

            self.networks[f"{net}"] = ip


    def get_loopback(self):
        res = self.interact.send("sh ip int br | include Lo")
        
        if(not "YES" in res):
            return False

        return res.split()[1]


    def add(self, to_add, area = 0):
        command = "router ospf 1\n"
       
        lo = self.get_loopback()
        if(lo):
            command += f"router-id {lo}\n"

        for net in to_add:
            base_ip = self.networks[net]
            command += f"network {base_ip} 0.0.0.0 area {area}\n"

        return self.interact.send(command, True)
        

    def show(self, res):

        print()
        s = False
        
        for line in res.split("\n"):
            if("router ospf" in line):
                s = True

            if(s):
                print(line)        

            if("end" in line):
                s = False

    def run(self):
        super().run()

        self.gather_networks()

        networks_question = questionary.checkbox(
            "Which networks do you want to route?",
            choices=[
                *list(self.networks.keys())
        ], qmark="?", instruction=" ").ask()

        if(not networks_question or networks_question == []): quit()

        res = self.add(networks_question)
        self.show(res)
