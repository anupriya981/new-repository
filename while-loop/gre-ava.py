list=[]
for i in range(1,6):
    i=int(input('enter the set of list:'))
    list.append(i)
    average=(sum(list))%(len(list))
    if i>average:

print(i)
