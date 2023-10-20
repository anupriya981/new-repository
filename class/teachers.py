class teachers:
    def teacher(self,teacher_8th,teacher_9th,teacher_10th):
        teacher_8th=input('enter 8th standerd teacher name:')
        teacher_9th=input('9th standerd teacher name:')  
        teacher_10th=input('10th standerd teacher name:')
        print(teacher_8th,teacher_9th,teacher_10th)

class students(teachers):
    def student(self,roll_no,class_div):
        roll_no=int(input('enter student roll_no:'))
        name=input('enetr name of syudent:')
        class_div=int(input('enter student div:'))
    
choice='y'
while choice=='y':
    choice=input('1:you want to conti Y/N\n2:student&teachers\n3:exit\nenter your option:')
    if choice==3:
        print('terminate programs')
    if choice==2:
        print(students)


