# c. Write a Python program to create an intersection, Union, difference of sets.
print('''Code written by
Samarth Dave
20ce019 ''')

#Created two Sets for performing operations on
MySet1 = {1,2,3,4,5}
MySet2 = {3,4,5,6,7,8,9}

#.intersection(SampleSet) for intersection of two sets 
print(f"Intersection of {MySet1} & {MySet2} is {MySet1.intersection(MySet2)}.")

#.union(SampleSet) for union of two sets 
print(f"Union of {MySet1} & {MySet2} is {MySet1.union(MySet2)}.")

#.Difference(SampleSet) for Difference of two sets 
print(f"Difference of {MySet1} & {MySet2} is {MySet1.difference(MySet2)}.")
print(f"Difference of {MySet2} & {MySet1} is {MySet2.difference(MySet1)}.")