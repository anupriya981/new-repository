list=[]
prime_num=[]
n=1
for num in range(1,6):
    num=input('enter the value:')
    list.append(num)
for i in num:
   for prime in range(2,int(i//2)+1):
    if prime==0:       
            prime_num.append(i)
    else:
       break 
print(prime_num)










#pending