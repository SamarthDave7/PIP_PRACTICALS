# c. Write a Python program to add an item in a tuple.


print('''Code written by
Samarth Dave
20ce019 ''')

#Created a tuple
MyTuple = (1, 2, 3, 4, 5)

#variable to store user input
num = int(input("Enter how many items do you want to add: "))

#FOR loop for inserting the number of elements entered by the user
for i in range(num):
    MyElement = int(input("Enter the Element you want to insert: "))

    #Formula to add new element in the tuple, (actually it makes the new tuple with same name)
    MyTuple += (MyElement,)

print(MyTuple)