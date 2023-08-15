# 54321
# 4321
# 321
# 21
# 1
#                             //   print number pattern in reverse order




num=int(input('enter the number:'))
for i in range(0,num+1):
    for j in range(num-i,0,-1):
       print(j,end=' ')
    
    print()
