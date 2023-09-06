print("a=c.v raman\nb=a.p.j abdulkalam\nc=rajendra prasad")
Q1=input("missile man of india:")
A1="a.p.j abdulkalam"
mark=0
if Q1==A1:
    print('correct answer')
    mark+=1
else:
    print("wrong answer")
    mark-=1

    print("a=c.v raman\nb=a.p.j abdulkalam\nc=rajendra prasad")
    Q2=input("indian physicist:")
    A2="c.v raman"
    if Q2==A2:
        print("correct answer")
        mark+=1
    else:
        print("wrong answer")
        mark-=1

    print("a=c.v raman\nb=a.p.j abdulkalam\nc=rajendra prasad")
    Q3=input("the first president of india:")
    A3="rajendra prasad"
    if Q3==A3:
        print("correct answer")
        mark+=1
    else:
        print("wrong answer")
        mark-=1

print("total mark",mark)