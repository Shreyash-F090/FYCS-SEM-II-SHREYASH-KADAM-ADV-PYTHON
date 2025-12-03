# F090 Shreyash Kadam
#-------------------------------------------------------------------------
class AgentDamage:
    def final_damage(F090, base_damage, headshot_multiplier):
        total = F090.calculate_damage(base_damage, headshot_multiplier) 
        print(f"Final Damage Dealt = {total}")
    def calculate_damage(F090, dmg, multi):
        return dmg * multi
agent = AgentDamage()
agent.final_damage(45, 3)
