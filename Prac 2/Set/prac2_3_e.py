# e Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
print('''Code written by
Samarth Dave
20ce019 ''')

################################## 1st. MOST COMMON ELEMENTS FROM LIST  #########################

#Created a list
Mylist = [1,3,5,6,3,2,12,5,2]

#List which holds the elements which are repeated only once (first typecasted to set and then to list)
Mylist2 = list(set(Mylist))

MaxNo = 0   #To store that how many times an element is repeated / are most common(Initialized with a zero)
Maxvalue = list([]) #To store the elements which are repeated maximum times / are most common

#FOR loop which checks in the original list by iterating the elements of the MyList2 and updating the value of count 
# for example i = 0  i.e.  Mylist2[0] = 1 -> MyList.count will check how many times 1 is repeated in the list MyList and later update the value of MaxNo.   
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])

#FOR loop to append the values of most common elements in the list called Maxvalues using the logic "Mylist.count(Mylist2[i]) = MaxNo" which returns the values that have count same as MaxNo.
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])

#FOR loop to print the values of the list Maxvlaue
for i in range(len(Maxvalue)) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in List\n")



################################ 2nd. MOST COMMON ELEMENTS FROM TUPLE  #########################

#Created a tuple
MyTuple = (1,2,4,6,3,2,1,2)

#List having same elements as of in tuple
Mylist = list(MyTuple) 

#List which holds the elements which are repeated only once (first typecasted to set and then to list)
Mylist2 = list(set(Mylist))

MaxNo = 0   #To store that how many times an element is repeated / are most common(Initialized with a zero)
Maxvalue = list([]) #To store the elements which are repeated maximum times / are most common

#FOR loop using the same logic as in line 16
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])

#FOR loop using the same logic as in line 21
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])

#FOR loop to print the values of the list Maxvlaue
for i in range(len(Maxvalue)) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in List\n")



############################## 3rd. MOST COMMON ELEMENTS FROM DICTIONARY  #######################

#Created a dictionary
Dic = {1:"I" , 2:"Ate" , 3:"Pizza" , 4:"I" , 5:"am" , 6 : "Fine"}

#List having same values as of in Dictionary
Mylist = list(Dic.values())

#List which holds the elements which are repeated only once (first typecasted to set and then to list)
Mylist2 = list(set(Mylist))

MaxNo = 0   #To store that how many times an element is repeated / are most common(Initialized with a zero)
Maxvalue = list([]) #To store the elements which are repeated maximum times / are most common

#FOR loop using the same logic as in line 16
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) > MaxNo :
        MaxNo = Mylist.count(Mylist2[i])

#FOR loop using the same logic as in line 21
for i in range(len(Mylist2)):
    if Mylist.count(Mylist2[i]) == MaxNo :
        Maxvalue.append(Mylist2[i])

#FOR loop to print the values of the list Maxvlaue
for i in range(len(Maxvalue)) :
    print(f"{Maxvalue[i]} is repeated {MaxNo} times in List\n")
