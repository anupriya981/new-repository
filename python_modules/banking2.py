import banking
choices='y'
while choices=='y' :
    choice=int(input('1:continue-y\n2:create bank_account\n3:view accound_status\n4:account balance-credit\n5:account balance-debited\n6exit-exit\n6:enter your choice:'))
    if choice==6:
        print('close the details')
        break
    elif choice==2:
        print('create an account')
        banking.details()
    elif choice==3:
        banking.view_account()
    elif choice==4:
        # option=input('credited/debited :')
        # if option=='credited':
        banking.credited_amount()
            # choice=input("Do you want to continue  y/n ")        
    elif choice==5:
        banking.deb()
    elif choice==6:
        exit()
    else:
        choice=input("enter a valid choice")

  
    
