# a=[-1,45,75,9,-436,47,-6,8,-4]
# tottal=0
# for i in range(0,len(a)):
#     tottal=tottal+a[i]
# print(tottal)
#//sum of list

a=[-1,45,75,9,-436,47,-6,8,-4]
a.sort()
a1=[]
tot=[0]
for i in a:
    if i>0:
        a1.append(i)
sum=sum(a1)
print(sum)



#a list of numbers as input and calculate the sum of all positive numbers