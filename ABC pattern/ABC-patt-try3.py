# A
# BC
# DEF
# GHIJ
# KLMNO
# PQRSTU


row=int(input('enter the row'))
count=1
for i in range(row):
    for j in range(0,i):
        print(chr(64+count),end='')
        count+=1
    print()