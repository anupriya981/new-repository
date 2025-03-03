#         *
#        ***
#       *****
#      *******
#     *********
#    ***********



# Function to print full pyramid pattern
n=int(input('enter the limit: '))
for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
        