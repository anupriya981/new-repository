value=[]
limit=int(input('enter the limit'))
for num in range(1,limit):
    num=int(input('enter the number:'))
    value.append(num)
i=0
sum=sum(value)
avg=sum//(len(value))
print("average is ",avg)
while i<len(value):
    values=(value[i])
    # print(values)
    i+=1
    if values>avg:
        print('great-',values)
        break
    else:
         continue


    