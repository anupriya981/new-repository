import banking
choice='y'
while choice=='y' :
    choice=int(input('1:continue-y\n2:create bank_account\n3:view accound_status\n4:account balance\n5:exit-exit\nenter your choice:'))
    if choice==5:
        print('close the details')
        break
    if choice==2:
        print('create an account')
        banking.details()
    if choice==3:
        banking.view_account()
    if choice==4:
        option=input('credited/debited :')
        if option=='credited':
            banking.credited_amount()
            choice=input("Do you want to continue  y/n ")        
        if option=='debited':
                banking.debited_amount()
    else:
        choice=input("Do you want to continue  y/n ")

  
    
