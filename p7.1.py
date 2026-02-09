import threading

def greet():
    print("Shreyash Kadam F090")

t = threading.Thread(target=greet)

t.start()

t.join()
