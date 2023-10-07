

choice='y'
i=1
while choice=='y':
    choice=input('continue Y/N:')
    if choice=='n':   
        print('program is terminated')
        exit()
    star=int(input('enter the limit:'))
    for i in range(star+1):
        print(i*'*')

#output
                                    # continue Y/N:y
                                    # enter the limit:3

                                    # *
                                    # **
                                    # ***
                                    # continue Y/N:n
                                    # program is terminated
