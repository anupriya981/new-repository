user_details={}
balance=0
account_details=[]
def details():
    user_name=input('enter your name:')
    user_adress=input('enter your adress:')
    user_age=int(input('enter your age:'))
    user_No=int(input('enter your contact number:'))
    account_no=65843691720
    

    user_details['user_name']=user_name
    user_details['user_adress']=user_adress
    user_details['user_age']=user_age
    user_details['user_No']=user_No
    user_details['account_no']=account_no
    user_details['balance']=balance

    account_details.append(user_details.copy())
    
def view_account():
    print(user_details)
    print(account_details)

def credited_amount():
    credit_amound=int(input('enter credited amound:'))
    for i in account_details:
        # print(i['balance'])

        balance=i['balance']

    # balance=user_details['balance']
        balance=balance+credit_amound
        user_details.update({'balance':balance+credit_amound})
        account_details.append(balance)





# def deb():
#     debit_amound=int(input('enter debited amound:'))
#     for i in account_details:
#         print(i)
#         # i['balance']=balance-debit_amound
#     print('hai')





def debited_amount():
    debit_amound=int(input('enter debited amound:'))
    for i in account_details: 
        #  print(i['balance'])
          i
       
        # balance=balance-debit_amound
        #   print(type(balance))
    #       user_details.update({'balance':balance-debit_amound})
    # account_details.append(balance)


    # print(balance)

