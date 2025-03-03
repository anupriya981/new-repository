details={}
name=input('enter name')
age=int(input('age'))
details['name']=name
details['age']=age
print(details)






details={}
name=input('enter name')
age=int(input('age'))
details[name]=age
print(details)



balance=0
details={}
detail=[]
name=input('name')
age=input('age')
details[name]=age
detail.append(details.copy())
# print(details)
# print('------')
# print(detail)
for i in detail:
    tottal=i[balance]
    print(tottal)

balance=0
mark=['jhdgf',28]
for i in mark:
    balance=i[balance]
    print(balance)
