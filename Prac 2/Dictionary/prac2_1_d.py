# d. Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
print('''Code written by
Samarth Dave
20ce019 ''')

# Created a dictionary
MyDictionary = {0:10,1:20}

#Created variables Key and Value to store the user input key and value
Key = int(input("Enter Your key : "))
Value = int(input(f"Enter value at {Key} : "))

# Formula for adding a key-value to the Dictionary
MyDictionary[Key] = Value

print(MyDictionary)