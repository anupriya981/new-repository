# data={}
# phy=int(input('physics:'))
# che=int(input('chemistry:'))
# mat=int(input('maths:'))
# eng=int(input('english:'))
# lan=int(input('language:'))


mark=[65,91,64,50,71]

def student(name):
    print(name)
name=input('name:')

def average(student):
    sum_mark=sum(mark)
    len_mark=len(mark)
    global avg_mark
    avg_mark=sum_mark%len_mark
    print(avg_mark)

def calculation(average):
    if avg_mark>=80:
        print('grad-A mark-',avg_mark)
    elif avg_mark>=60 and avg_mark<=80:
        print('grad-B mark-',avg_mark)
    elif avg_mark>=50 and avg_mark<=60:
        print('grad-c mark-',avg_mark)
    else:
        print('fail mark-',avg_mark)

