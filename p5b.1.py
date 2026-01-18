class Valo:
    def __init__(F090, Agent, Role):
        F090.Agent = Agent
        F090.Role = Role

    def info(F090):
        print(f"I am a Agent. My name is {F090.Agent}. My Role {F090.Role}.")

    def make_sound(F090):
        print("know what must be done")


class BGMI:
    def __init__(F090, name, age):
        F090.Character = name
        F090.age = age

    def info(F090):
        print(f"I am a character in bgmi. My name is {F090.Character}. I am {F090.age} years old.")

    def make_sound(F090):
        print("follow me")


Valo1 = Valo("sage", "Sentinels")
BGMI1 = BGMI("Sara", 24)

for Game in (Valo1, BGMI1):
    Game.make_sound()
    Game.info()
    Game.make_sound()
