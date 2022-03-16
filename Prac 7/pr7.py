T = int(input()) #for taking number of inputs 

string=[]
for tc in range(T):
    string.append(input())

for tc in range(T):
    s = str(string[tc])
    # two empty strings to be concatenated
    s1,s2='',''

# Checking the string length, to divide the string in equal parts
    if(len(s)%2==0):#IF STRING LENGTH IS EVEN
        s1=s[:len(s)//2] 
        s2=s[len(s)//2:]

    else: # IF THE STRING LENGTH IS ODD (it omits the middlemost character of that string)
        s1=s[:len(s)//2]
        s2=s[len(s)//2+1:]

        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()

        s1=str(l1)
        s2=str(l2)
# checking the strings and printing the required output
    if(s1==s2):
        print('YES')
    else: 
        print('NO')