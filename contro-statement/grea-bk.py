#WAP to that take a list of words as input and finds the first word with more then five charectop using a for loop and break statement


list=[]
r=[]
for num in range(1,6):
    num=input('enter the charector:')
    list.append(num)
for i in list:
    if len(i)<5:
         r.append(i)
    else:
         break
print(r)













# r=[]
# num=['arya','diya','divya','kavya','fu']
# for i in num:
#     if len(i)<5:
#          r.append(i)
#     else:
#          break
# print(r)