# 123456
# 12345
# 1234
# 123
# 12
# 1
#                         print number pattern in revers order



limit=int(input('enter the limit:'))
for i in range(0,limit+1):
    for j in range(1,limit-i):
        print(j,end='')
    print()