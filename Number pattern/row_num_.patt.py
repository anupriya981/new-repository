# 1
# 2 3
# 4 5 6
# 7 8 9 10




lim=int(input('entere the row:'))
current_no=1
for i in range(1,lim+1):
    for j in range(i):
        print(current_no,end=' ')
        current_no+=1  
    print()
         



