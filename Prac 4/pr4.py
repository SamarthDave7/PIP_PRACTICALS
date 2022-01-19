print('''Code written by
Samarth Dave
20CE019''')

#variable for input 
n = int(input())
arr = map(int, input().split())

print(sorted(list(set(arr)))[-2])