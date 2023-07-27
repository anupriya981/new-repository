side1=int(input("enter the fir-leng:"))
side2=int(input('enter the sec-length:'))
side3=int(input('enter the thir-leng'))
if side1==side2 or side1==side3 or side2==side3:
    print("isosceles")
    if side1==side2==side3:
        print('equilateral')
else:
        print('scalene')
