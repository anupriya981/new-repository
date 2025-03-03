n = int(input('enter the limit: '))

for i in range(1,n+1):
    print(" "*(n-1), end=" ")
    for j in range(2,100):
        while j<1:
            if (j/i)==0:
                break
        else:
            print(j)