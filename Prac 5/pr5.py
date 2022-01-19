print('''Code written by
Samarth Dave
20CE019''')
s = input()

Output = ''
for char in s:
    if(char.isupper()==True):
        Output += (char.lower())
    elif(char.islower()==True):
        Output += (char.upper())
    else:
        Output += char
print(Output)