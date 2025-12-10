# F090 Shreyash Kadam
class Agent:
    def show_agent(F90):
        print("Agent: Base Valorant Agent")

class Duelist(Agent):
    def ability(F90):
        print("Duelist Ability: Entry Fragging")

class Initiator(Agent):
    def ability(F90):
        print("Initiator Ability: Recon / Info Gathering")

s = Duelist()
f = Initiator()

s.show_agent()
s.ability()

f.show_agent()
f.ability()
