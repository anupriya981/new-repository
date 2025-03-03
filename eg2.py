# f=open('priya','w')
# f.write('shgdfiysgtfoerg')
# f.close()

# uni=[]
# dup=[]
# my_list = [1,2,3,6,3,9,2]
# for i in my_list:
#     # print(i)
#     if i not in uni:
#         uni.append(i)
#     elif  i in uni:
#         dup.append(i)
# print(dup)
# print(uni)
            
# squre = []
# for i in range(1,4):
#     num=int(input('enter no: '))
#     squr= num**2
#     squre.append(squr)
#     sums=sum(squre)
# print(sums)
    
    
side = int(input('enter no: '))
for i in range(1,side):
    print('*' *i+''*i)