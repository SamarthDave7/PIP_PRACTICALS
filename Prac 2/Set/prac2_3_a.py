# a. Write a Python program to add member(s) in a set and clear a set

print('''Code written by
Samarth Dave
20ce019 ''')

#Created a Set
MySet = {1, 2, 3, 4, 5}
print(f"Old set : {MySet}")

#User input for choices
UserInput = int(input("Enter 1 for adding elements in set and 2 for clearing set: "))
#IF-ELSE for the respective choices
if(UserInput==1):

    #for the number of times user want to add elements
    num = int(input("Enter the number of elements you want to add: "))

    #FOR loop for adding the inputs given by user
    for i in range (num):
        MySet.add(int(input("Enter the element: ")))

    print(f"New set after adding the elements: {MySet}")

elif(UserInput==2):
    #For clearing the contents of SET
    MySet.clear()
    print(f"New set after clear : {MySet}")

else:
    print("Please select a valid choice!")