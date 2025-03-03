limit=int(input('enter the limit:'))
for i in range(limit):
    for k in range((i,limit-i)):
     print(' ',end='')
     for j in range(0,i,2):
        print(j,end='')
    print()