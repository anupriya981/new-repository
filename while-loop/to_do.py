# print('to_do')
# do=[]
# choice=(input('add/exit:'))
#  while choice=='add':
#     data=(input('do:'))
#     do.append(data)

#     if choice=='exit':
#       break




mylist=[]
choice='n'
while choice!='N':
    print('='*5,'ToDo','='*5)
    print('''1. Add Schedule
    2. Remove Schedule
    3. View Schedule
    4. Exit

    ''')
    
    choice=int(input('please enter your choice' ))

    if choice==1:
        element=input('enter your schedule ')
        mylist.append(element)
    elif choice==2:
        element=input('enter the schedule you want to remove ')
        mylist.remove(element)
    elif choice==3:
        print('='*5,'Todays Schedule','='*5)
        for i in mylist:
            print(i)
    elif choice==4:
        print('thanks for using todo application')
        exit()
    else:
        print('you have entered a invalid choice')
        choice=input("Do you want to continue  y/n ")
