#Shreyash Kadam F090
from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def reload(self):
        pass

class Vandal(Weapon):

    def fire(self):
        print("Vandal firing ")

    def reload(self):
        print("Vandal reloading ")


v = Vandal()
v.fire()
v.reload()
