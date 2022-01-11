# Dictionary

# a. Write a Python script to check whether a given key already exists in a dictionary.

Dic = {1:"Rabbit",2:"is",3:"very",4:"Cute"}

Mylist = list(Dic.keys())
Key = input("Enter Your key : ")

if Mylist.__contains__(Key) :
    print("Key already exists in a dictionary.")
else :
    print("Key does not exists in a dictionary.")

