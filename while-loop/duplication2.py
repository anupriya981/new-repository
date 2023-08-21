dup=[]
ori=[]
str=input('enter the string:')
i=0
while i<len(str):
    stri=(str[i])
    # print(stri)
    if stri not in ori:
        ori.append(stri)
        
    else:
        dup.append(stri)
    i+=1
print(dup)