# d. Write a Python program to convert a tuple to a string.
from typing import Tuple


print('''Code written by
Samarth Dave
20ce019 ''')

#Created a tuple to which we have to convert to string
MyTuple = ("P", "I", "Z", "Z", "A")
print(f"Old type : {type(MyTuple)}")

# created an empty string
MyString = ""

#FOR loop to concatenate the string with the elements of the tuple
for i in range(len(MyTuple)):
    MyString += MyTuple[i]

#new tuple for adding the string as an element(Rightnow the new tuple is a tuple class)
NewTuple = (MyString)

#New tuple is converted to a string type
NewTuple = str(NewTuple)
print(f"New type : {type(NewTuple)}")

print(NewTuple)