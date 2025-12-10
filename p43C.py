# F090 Shreyash Kadam
class Agent:
    def show_agent(F90):
        print("Agent: Reyna")

class Role(Agent):
    def show_role(F90):
        print("Role: Duelist")

class Ability(Role):
    def show_ability(F90):
        print("Ability: Devour (Self-Heal)")


F090 = Ability()
F090.show_agent()     
F090.show_role()     
F090.show_ability()   
