# A
# B A
# C B A
# D C B A
# E D C B A


row=int(input('enter the row:'))
for i in range(row):
    for j in range(i+1,0,-1):
        print(chr(64+j),end=' ')
    print()

