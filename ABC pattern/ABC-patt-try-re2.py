row=int(input('enter the row'))
for i in range(row,0,-1):
    for j in range(i+1,0,-1):
        print(chr(65+j),end='')
    print()