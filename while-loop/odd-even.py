odd=[]
even=[]
i=0
while i<100:
    i+=1
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('odd-',odd)
print('even-',even)