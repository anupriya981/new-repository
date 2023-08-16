# print ABC pattern in python
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E



row=int(input('enter the row:'))
for i in range(row):
    for j in range(row):
        print(chr(65+j),end=' ')
    print()

 

# FEDCBA
# FEDCBA
# FEDCBA
# FEDCBA
# FEDCBA



row=int(input('enter the row:'))
for i in range(row):
    for j in range(row,0,-1):
        print(chr(64+j),end=' ')
    print()