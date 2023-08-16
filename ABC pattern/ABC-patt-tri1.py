# A
# A B
# A B C
# A B C D
# A B C D E



row=int(input('enter the row:'))
for i in range(row):
    for j in range(0,i+1):
        print(chr(65+j),end=' ')
    print()