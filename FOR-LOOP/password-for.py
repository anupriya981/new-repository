# pending
pwd=input("enter the password:")
for i in pwd:
    if len(pwd)<=8 and pwd>='a' and pwd<='z' and pwd>='A' and pwd<='Z' and pwd>=1 and pwd<=9:
        print('password create successfully')
else:
    print('should be at least 8 cahr long\n should contain at least one uppercase letter\nshould contain at least one loweercase\nshould contain at least one digit')

