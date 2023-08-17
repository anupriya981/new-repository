# A B C D E
# F G H I
# J K L
# M N
# O





row=int(input('enter the row:'))
count=1
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(chr(64+count),end=' ')
        count+=1
    print()