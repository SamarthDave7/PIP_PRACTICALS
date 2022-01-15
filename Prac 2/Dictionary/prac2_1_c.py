# c. Write a Python program to sum all the items in a dictionary.

print('''Code written by
Samarth Dave
20ce019 ''')

#Created a dictionary

MyDictionary = {1:100,2:200,3:300,4:400}

# Created an list to store values of dictionary
Arr = list(MyDictionary.values())

sum = 0
#FOR LOOP for updating the value of sum by taking each of the element from the list
for i in range(len(Arr)):
    sum += Arr[i]
    i += 1

print(sum)