#Shreyash Kadam
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
pass
def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return num
try:
    number = int(input("Enter a positive number: "))
    check_positive(number)
    print("Valid number entered!")
except NegativeNumberError as e:
    print(f"Error: {e}")
