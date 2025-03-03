# for num in range(1,100):
#       if num>1:
#          for i in range(2,num):
#             if (num % i)==0:
#                break
#          else:
#             print(num)
# limit=int(input('enter the limit: '))         
limit = 5
my_list = []          
for num in range(1,100):
   if num>1:
      for i in range(2,num):
         if (num % i) == 0:
            break
      else:
         my_list.append(num)
print(my_list)

for n in range(my_list):

   for j in range(1,limit+1):
      print(' '*(limit-1), end=" ")
      for k in range(21,j):
       print(n, end=" ")
   print()



