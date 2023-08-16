# print ABC pattern in python
# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE

row=int(input('enter the number:'))
for i in range(row):
    for j in range(row):
        print(chr(65+i),end='')
    print()