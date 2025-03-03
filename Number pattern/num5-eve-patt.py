# 0
# 02
# 024
# 0246
# 02468
#                             print the even number pattern in python



limit=int(input('enter the limit:'))
for i in range(0,limit+1,2):
    for j in range(0,i,2):
        print(j,end='')
    print()