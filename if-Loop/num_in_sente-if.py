# wrd=input('enter the number in words:')
# if wrd>0 and wrd<=9:
#     if wrd=='one':
#         print('1')
#     if wrd=='two':
#         print('2')
# if wrd=='three':
#     print('3')
# if wrd=='four':
#     print("4")
# if wrd=='five':
#     print('5')
# if wrd==('six'):
#     print('6')
# if wrd==('seven'):
#     print('7')
# if wrd==('eight'):
#     print('8')
# if wrd=='nine':
#     print('9')






wrd=input('enter the number in words:')
num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
for i,j in num.items():
   # print(i,j)
    if wrd==i:
     print('the value is:',j)
    