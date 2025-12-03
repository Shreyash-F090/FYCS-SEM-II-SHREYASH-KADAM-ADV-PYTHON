# F090 Shreyash Kadam
#-----------------------------------------------------------------------------------------------
class Skye:
    def __init__(F090):
        F090.name = "Skye"
        F090.role = "Initiator"
        F090.power = 100
        print("[AGENT] Skye — The Wilderness Warrior")
    def profile(F090):
        print("\n--- SKYE PROFILE ---")
        print(f"Name  : {F090.name}")
        print(f"Role  : {F090.role}")
        print(f"Power : {F090.power}")
    def use_ability(F090, ability, cost):
        if F090.power < cost:
            print(f"Skye doesn’t have enough energy to use {ability}!")
            return
        F090.power -= cost
        print(f"Skye casts **{ability}** (-{cost} energy). Remaining: {F090.power}")
    def heal_team(F090, amount):
        print(f"Skye heals her team for {amount} HP using **Regrowth** 6")
        F090.power -= 15
        if F090.power < 0:
            F090.power = 0
        print(f"Energy after healing: {F090.power}")
    def recharge(F090, amount):
        F090.power += amount
        if F090.power > 100:
            F090.power = 100
        print(f"Skye connects with nature and restores +{amount} energy. Total: {F090.power}")
agent = Skye()
agent.profile()
agent.use_ability("Trailblazer (Tasmanian Tiger)", 30)
agent.heal_team(45)
agent.recharge(20)
agent.use_ability("Guiding Light (Falcon Flash)", 25)
agent.profile()
