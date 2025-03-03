print("a=c.v raman\nb=a.p.j abdulkalam\nc=rajendra prasad")
Q1=input("missile man of india:")
A1="b"
mark=0
if mark==0:
    if Q1==A1:
     print('correct answer.........')
     mark+=1
    else:
     print("wrong answer........")
     mark-=1

    print("a=c.v raman\nb=a.p.j abdulkalam\nc=rajendra prasad")
    Q2=input("indian physicist:")
    A2="a"
    if Q2==A2:
        print("correct answer......")
        mark+=1
    else:
        print("wrong answer.......")
        mark-=1

    print("a=c.v raman\n b=a.p.j abdulkalam\n c=rajendra prasad")
    Q3=input("the first president of india:")
    A3="c"
    if Q3==A3:
        print("correct answer.........")
        mark+=1
    else:
        print("wrong answer.........")
        mark-=1
        print("total mark",mark)
        if mark ==-3:
            print("not eligible")
else:
 print("thank you ")
 