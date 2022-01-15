# a. Write a Python program to create a tuple with different data types.
print('''Code written by
Samarth Dave
20ce019 ''')

# Created a Tuple with different datatypes
MyTuple = (7,'Samarth',1.9, True)
print(MyTuple)

#For loop for printing the datatype of each element of the tuple
for i in range(len(MyTuple)):
    print(type(MyTuple[i]))
