user_details={}
def details ():
    user_name=input('enter your name:')
    user_adress=input('enter your adress')
    user_age=int(input('enter your age'))
    user_No=int(input('enter your contact number'))
    account_no=65843691720

    user_details['user_name']=user_name
    user_details['user_adress']=user_adress
    user_details['user_age']=user_age
    user_details['user_No']=user_No
    user_details['account_no']=account_no
    print(user_details)