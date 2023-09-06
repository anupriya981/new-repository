value=int(input("enter the total purchase:"))
if value>=100:
    tot=(value*10)/100
    print( "10 persentage discount:",value-tot)
else:
        print("no dicount")