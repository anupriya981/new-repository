# *****
#  ****
#   ***
#    **
#     *
limit=(int(input('enter the limit:')))
for i in range(limit,0,-1):
    print(" "*(limit-i)+'*'*i)
    
    
# *****
# ****
# ***
# **
# *

for i in range(limit,0,-1):
    print('*'*i+" "*(limit-i))

