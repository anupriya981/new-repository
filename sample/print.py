# print("print(hello)")



balance=50
# amound=int(input('amound:'))
# balance-=amound
# print(balance)



option=input('credited/debited :')
if option=='credited':
    credit_amound=int(input('enter credited amound:'))
    balance+=credit_amound
    print(balance)
elif option=='debited':
    debit_amound=int(input('enter debited amound:'))
    balance-=debit_amound
    print(balance)
     
    # if choice==5: