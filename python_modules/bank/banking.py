user_details={}
balance=0
account_details=[]
account_num=65843691720
def details():
    user_name=input('enter your name:')
    user_adress=input('enter your adress:')
    user_age=int(input('enter your age:'))
    user_No=int(input('enter your contact number:'))
    account_no=account_num

    user_details['user_name']=user_name
    user_details['user_adress']=user_adress
    user_details['user_age']=user_age
    user_details['user_No']=user_No
    user_details['account_no']=account_no
    user_details['balance']=balance

    account_no+=1
    account_details.append(user_details.copy())
    
def view_account():
    print(user_details)
    # print(account_details)

def credited_amount():
    conf_acc_no=int(input('conform your account no:'))
    credit_amound=int(input('enter credited amound:'))
    bank_account=account_details.copy()
    global total
    total = balance+credit_amound
    bank_acc=[]
    # print(account_num)
    for i in bank_account:
        bank_acc.append(total)
    print('\n amound sucessfuly credited,\n credit_amound :  ',credit_amound, '\ntotal balance: ',total)
    if conf_acc_no in bank_acc:

        for i in bank_account:
            print('accno is',i['account_num'])
            if i[account_num]==conf_acc_no:
                balance=i['balance']
                print(balance)
                i.update({'balance':balance+credit_amound})

            else:
                print('account no is not found')


    # balance=user_details['balance']
        # balance=balance+credit_amound
    # account_details.append(user_details.copy())

# def deb():
#     debit_amound=int(input('enter debited amound:'))
#     for i in account_details:
#         print(i)
#         # i['balance']=balance-debit_amound
#     print('hai')


def debited_amount(credited_amount):
    debit_amound=int(input('enter debited amound:'))
    for i in account_details: 
        #  print(i['balance'])
          balance=i['balance']
          
       
          balances = total - debit_amound
          print('debited amound: ',debit_amound)
          print('remain balance: ',balances)
          user_details.update({'balance':balance-debit_amound})
    # account_details.update('balance')


    print('available balane:  ',balance)

