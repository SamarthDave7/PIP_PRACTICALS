# a. Write a Python script to check whether a given key already exists in a dictionary.

print('''Code written by
Samarth Dave
20ce019 ''')

#Created a dictionary
MyDictionary = {1:"I",2:"ate",3:"Pizza",4:"Today"}

# Created an list to store keys of dictionary
Arr = list(MyDictionary.keys())

# Created variable Key to store the input given by the user
Key = int(input("Enter Your key : "))


#IF-ELSE that Checks that Key is in the list or not
if Key in Arr: 
     print("Key already exists in a dictionary.")
else :
    print("Key does not exists in a dictionary.")

