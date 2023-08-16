# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY
#                                           PRINT ABC PATTERN IN PYHON



row=5
count=0
for i in range(row):
    for j in range(row):
         print(chr(65+count),end='')
         count+=1
    print()


