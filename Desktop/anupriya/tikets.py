age=int(input("enter your age:"))
day=input('enter the day:')

if (age<12 or age>65):
    print("RS:5")
elif (12>=age or age<=18 and day=="wed"):
            print("RS:4")
else:
      print("RS:10")
            
    