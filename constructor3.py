# F090 Shreyash Kadam
#--------------------------------------------------
agent_name = "Skye"
kills = 18
assists = 4
class Performance:
    def calculate_score(self):
        score = (kills * 2) + assists
        print(f"Agent: {agent_name}")
        print(f"Final Performance Score = {score}")
p1 = Performance()
p1.calculate_score()
