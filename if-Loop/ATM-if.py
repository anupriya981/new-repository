bal=int(input("enetr your accnt balance:"))
option=input('withdraw / deposit:')
if option=='withdraw':
        amou=float(input("amound:"))
        if bal>amou:
            balance=bal-amou
        else:
            print("inefitial balane")
elif  option=='deposit':
    amou=float(input("amound:"))
    balance=bal+amou
    print('remaining balance:',balance)
else:
    print('somthing ewnt wrong.......please try again')
 