char=input('enter the charector:')
if ((char>='a' and char<='z') or( char>='A' and char<='Z')):
    print(char,'is alphabet')
elif (char>='0' and char<='9'):
    print(char,'is digit')
else :
    print(char,'special charector')

#write a pgm to check whether a charector is an alphabet ,digit or special cherector