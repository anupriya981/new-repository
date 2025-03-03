#       0 
#      1 1 
#     2 2 2
#    3 3 3 3
#   4 4 4 4 4

# n=int(input('enter the limit: '))
n = 5
num=1
for i in range(0, n):
    print(" "*(n-i), end=" ")
    for j in range(0, i+1):
        print(i, end=" ")
    print()
    
print(15*'*')
    
#      1 
#     2 3 
#    4 5 6
#   7 8 9 10

n = 4
num = 1
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1
    print()
    
