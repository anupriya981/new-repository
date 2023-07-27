print('eligibility critiria')
math=int(input("mark in maths:"))
phy=int(input("mark in physics:"))
che=int(input("merk in che:"))
tot=math+phy+che
print('total mark',tot)
if tot>=190 or math+phy==140:
    print("eligible")
    
else:
    print('not eligible')






    #write a pgm to determine eligible for admission to a professional course based on the followng critiria