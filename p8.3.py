#Shryeash KadamS
try:
    file = open("non_existent_file.txt", "r")
except Exception as e:
    print(f"An error occurred: {e}")
