num=int(input('enter the limit:'))
for i in range(1,num):
    for j in range(1,num,1+i):
        print(j,end='')
    print()