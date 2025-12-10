# F090 Shreyash Kadam
class Agent:
    def show_agent(F90):
        print("Agent: Phoenix")

class Role:
    def show_role(F90):
        print("Role: Duelist")

class DuelistAgent(Agent, Role):
    def ability(F90):
        print("Ability: Hot Hands (Self-heal)")


F090 = DuelistAgent()
F090.show_agent()   
F090.show_role()    
F090.ability()      
