balances=[]
bal=int(input("enetr your accnt balance:"))
balances.append(bal)
option=input('withdraw / deposit:')
if option=='withdraw':
    amou=float(input("amound:"))
    balance=bal-amou
elif  option=='deposit':
    amou=float(input("amound:"))
    balances.append(amou)
    
    balance=sum(balances)


print('remaining balance:',balance)
