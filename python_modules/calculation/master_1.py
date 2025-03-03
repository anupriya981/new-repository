#     create a python program to print arithemetic calculation using sum,product,difference,factorial,squre

def sum():
      num1=int(input('enter the num1: '))
      num2=int(input('enter the num2: '))
      print (num1+num2)
    
def  product():
    num1=int(input('enter the num1: '))
    num2=int(input('enter the num2: '))
    print(num1*num2)   
    
def difference():
    num1=int(input('enter the num1: '))
    num2=int(input('enter the num2: '))
    print(num1-num2)

def squre():
    num1=int(input('enter the num1: '))
    num2=int(input('enter the num2: '))
    print(num1**num1,num2**num2)
     
def factorial():
     num=int(input('enter the numbaer:'))
     fact=1
     for i in range(1,num+1):
        fact=fact*i
     print(fact)
    