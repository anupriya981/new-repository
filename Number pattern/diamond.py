#      10
#     11 12
#    13 14 15
#   16 17 18 19
#  20 21 22 23 24
#   25 26 27 28
#    29 30 31
#     32 33
#      34

n = int(input('enter limit: '))
num = 10
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1
    print()
    
for i in range(n-1,0,-1):
    print(" "*(n-i), end=" ")
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()