# write a program that take a list of integer as input and remove all the duplicates from the list using while loop?
            # eg:enter the string:ammu
            #    ['a', 'm', 'u']



dup=[]
ori=[]
str=input('enter the string:')
i=0
while i<len(str):
    stri=(str[i])
    # print(stri)
    if stri not in dup:
        dup.append(stri)
    if stri  in dup:
        ori.append(stri)
    i+=1
print(dup)
print(ori)




       
