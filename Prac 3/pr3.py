print('''Code written by
Samarth Dave
20CE019''')

N = int(input())
rooms = list(map(int, input().split(' ')))
seen = {}

#for loop for checking and increasing the value of the key
for i in rooms:
    if not i in seen:
        seen[i] = 1
    else:
        seen[i] += 1

#Cheking and the n printing the key having the value 1
for Key, val in seen.items():
    if val != N:
        print(Key)