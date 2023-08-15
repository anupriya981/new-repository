# 1
# 13
# 135
# 1357
#                                 print number pattern in python



# limit=int(input('enter the limit:'))
# for i in range(1,limit+1,2):
#     for j in range(1,i,2):
#         print(j,end='')
#     print(i)




limit=int(input('enter the limit:'))
for i in range(1,limit+1):
    for j in range(1,i):
      if(j%2==1):
         print(j,end='')
    print()