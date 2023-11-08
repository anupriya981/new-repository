mark=[]
phy=int(input('physics:'))
che=int(input('chemistry:'))
# mark.apppend(che)
mat=int(input('maths:'))
# mark.apppend(mat)
eng=int(input('english:'))
# mark.apppend(eng)
lan=int(input('language:'))
mark.append(phy)
mark.append(che)
mark.append(mat)
mark.append(eng)
mark.append(lan)











# mark=[82,94,55,68,66]
def student(name):
    print(name)
name=input('name:')

def average():
    sum_mark=sum(mark)
#     print(sum_mark)
    len_mark=len(mark)
    global avg_mark
    avg_mark=sum_mark/len_mark
#     print(avg_mark)
average()
print(name)
print('average mark is',avg_mark)


if avg_mark>=80:
        print('grad-A ')
elif avg_mark>=60 and avg_mark<=80:
       print('grad-B ')
elif avg_mark>=50 and avg_mark<=60:
       print('grad-c ',)
else:
       print('fail ',)


