vow=['a','e','i','o','u']
l1=[]
i=0
char='education'
while i<len(char):
    cha=(char[i])
    i+=1
    if cha==vow:
        l1.append((cha))

        print(l1)
else:
    print('there is no vowals')
        
