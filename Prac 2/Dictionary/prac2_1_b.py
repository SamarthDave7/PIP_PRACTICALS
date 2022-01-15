# b. Write a Python script to merge two Python dictionaries.

print('''Code written by
Samarth Dave
20ce019 ''')

#Created two dictionaries to be merged
MyDictionary1 = {1:"This",2:"is",3:"very",4:"Hot"}
MyDictionary2 = {5:"Food"}

#used .update to update the dictionary 1 with the contents of the given arguement
MyDictionary1.update(MyDictionary2)

print(MyDictionary1)