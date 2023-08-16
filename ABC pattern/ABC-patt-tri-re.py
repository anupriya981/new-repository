
# EDCBA
# DCBA
# CBA
# BA
# A
  



row=int(input('enter the row:'))
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(chr(64+j),end=' ')
    print()
