#Shreyash Kadam F090
import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

def print_letters():
    for char in "ABCDE":
        print(f"Letter: {char}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads finished execution.")
