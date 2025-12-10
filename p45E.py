# F090Shreyash Kadam
class Agent:
    def show_agent(F90):
        print("Agent: Yoru")

class Duelist(Agent):
    def show_role(F90):
        print("Role: Duelist")

class Initiator(Agent):
    def show_info(F90):
        print("Initiator: Provides intel and support")

class Ultimate(Duelist):
    def show_ultimate(F90):
        print("F090ltimate: Dimensional Drift")

F090 = Ultimate()
F090.show_agent()    
F090.show_role()     
F090.show_ultimate() 
