bal=int(input("enetr your accnt balance:"))
option=input('withdraw / deposit:')
if option=='withdraw':
    amou=float(input("amound:"))
    balance=bal-amou
elif  option=='deposit':
    amou=float(input("amound:"))
    balance=bal+amou

print('remaining balance:',balance)
