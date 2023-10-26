teachers_list=['nimisha','arjun','arnouve','yadhav']
details={}
    

def students():
    stu_clss=int(input('enter the class of student:'))
    stu_roll=int(input('roll number of student:'))
    stu_name=input('enter the name of student:')

    details['stu_clss']=stu_clss
    details['stu_roll']=stu_roll
    details['stu_name']=stu_name
    print(details)

