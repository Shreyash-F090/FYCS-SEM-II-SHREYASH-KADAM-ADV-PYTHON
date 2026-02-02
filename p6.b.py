#Shreyash Kadam F090

from abc import ABC, abstractmethod

class Agent(ABC):

    @abstractmethod
    def use_ability(self):
        pass

class Phoenix(Agent):

    def use_ability(self):
        print("Phoenix uses Fire Wall ")

p = Phoenix()
p.use_ability()
