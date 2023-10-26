import teachers
choice='y'
while choice=='y':
    choice=input('1:you wnat to continue Y/N\n2:students&teachers\n3:exit\nenter your choice')
    if choice==3:
        print('the program is terminated')
        exit
    if choice==2:
        teachers.students()
        print('detals')
        
    