# b. Write a Python program to remove an item from a set if it is present in the set.
print('''Code written by
Samarth Dave
20ce019 ''')

#Created a Set
MySet = {1, 2, 3, 4, 5}
print(f"Set : {MySet}")

#Variable to store the user input
MyElement = int(input("Enter the element you want to remove: "))

#IF-ELSE loop for checking the user input element is present or not
if MyElement in MySet:

    #.remove(element_to_remove) function to remove from the given set
    MySet.remove(MyElement)
    print(f"{MyElement} removed.")
    print(f"New set : {MySet}")
    
else:
    print(f"{MyElement} is not present in the set.")