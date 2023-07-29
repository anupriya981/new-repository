# l=['a','b','m','a','c','a','b']
# d=[]
# for i in l:
#   if l.count(i)>1:
#      d.append(i)
#      f=set(d)
#      f=list(f)












# l=['a','b','m','a','c','a','b']
# d=[]
# for i in l:
#     eq=l.count(i)
#     if 1<eq:
#      print('duplicates')
#      d.update({eq:i})
#     else:
#        print('no duplicates')
# print(d)




#                                                                   copy paste

# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
# uni = []
# dup = []
 
# for i in lis:
#     if i not in uni:
#         uni.append(i)
#     elif i not in dup:
#         dup.append(i)
 
# print(dup)





from collections import Counter
my_list =['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
my_counter=Counter(my_list)
print(my_counter)
