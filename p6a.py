#Shreyash Kadam F090
from abc import ABC

class Agent(ABC):
    pass

class Jett(Agent):
    def role(self):
        print("Jett is a Duelist")

j = Jett()
j.role()
