print('''Code written by
Samarth Dave
20CE019''')

N = int(input())
d = dict({})

for i in range(N):
    word = input()
    if word in d:
        d[word] +=1
    else:
        d[word] = 1

print(len(d))

for v in d.values():
    print(v,end = " ")