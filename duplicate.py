# l=['a','b','m','a','c','a','b']
# d=[]
# for i in l:
#   if l.count(i)>1:
#      d.append(i)
#      f=set(d)
#      f=list(f)












l=['a','b','m','a','c','a','b']
d=[]
for i in l:
    eq=l.count(i)
    if 1<eq:
     print('duplicates')
     d.update({eq:i})
    else:
       print('no duplicates')
print(d)




