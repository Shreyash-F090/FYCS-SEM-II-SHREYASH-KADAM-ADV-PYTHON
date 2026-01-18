class Points:
    def __init__(F090, x):
        F090.x = x

    def __add__(F090, other):
        return F090.x + other.x

p1 = Points(90)
p2 = Points(90)

print("Addition:", p1 + p2)
print("Shreyash Kadam F090")
