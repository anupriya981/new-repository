import teachers
teachers_list=['1.nimisha','2.arjun','3.arnouve','4.yadhav']
choice='y'
while choice=='y':
    choice=input('1:you wnat to continue Y/N\n2:detils of teachers\n3:display your choice\n4:exit\nenter your choice:')
    if choice==4:
        print('program is terminated:')
        exit
    if choice==2:
        # teachers_list=['1.nimisha','2.arjun','3.arnouve','4.yadhav']
        print(teachers_list)
        
    