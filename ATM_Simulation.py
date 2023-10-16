message = " please choose your option 1 --> check balance , 2 ---> deposit amount  ,3 --> withdrawl amount"
print(message)
task = int(input('enter your option :-'))
available_amount = 5000

if (task >=1) and (task <=3):
    if task == 1:
        # 1 balance
        check_message = f"your available balance is :- {available_amount}"
        print(check_message)
        
    elif task == 2:
        deposit_amount = int(input('please enter your deposit amount :-'))
        if deposit_amount > 0:
            available_amount += deposit_amount
            print('your amount successfullly deposit')
            check_message = f"your available balance is :- {available_amount}"
            print(check_message)

        else:
            print('please give your valuable amount')


    else:
        withdrawl_amount = int(input('please enter your withdrawl amount :-'))
        if withdrawl_amount <= available_amount:
            available_amount -= withdrawl_amount
            print('you have successfully withdrawl your amount :- ',withdrawl_amount)
            check_message = f"your available balance is :- {available_amount}"
            print(check_message)

        else:
            print('pese nahi he')    
else:
    print('please correct option')

