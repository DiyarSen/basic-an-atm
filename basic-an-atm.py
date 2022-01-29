print("""\tHello, Welcome to The X Bank
\tPlease Insert Your Credit Card...""")

example_data_base = {
    "account-first": {
        "name": "Diyar",
        "surname": "Şen",
        "card-password": "1234",
        "account-balance": int(5000),
        "account-debt": int(4000),
        "account-debt-deadline": "02/03/2022"},

    "account-second": {
        "name": "Ferit",
        "surname": "Şen",
        "card-password": "5678",
        "account-balance": int(8000),
        "account-debt": int(6000),
        "account-debt-deadline": "06/04/2022"}
}

the_card = dict(example_data_base["account-second"])

right = 2

for i in range(0, 3):
    password = input("Please enter your 4 digit password: ")

    if password == the_card.get("card-password"):
        print("""Welcome to your X Bank account {} {}
        Please select the action you want to do...""".
        format(the_card.get("name"), the_card.get("surname")))

        action_select = input("""
        [1] Balance Inquiry
        [2] Debt Inguiry
        [3] Withdraw
        [4] Deposit
        [Q] Exit\n""")
        
        break

    elif password != the_card.get("card-password") and right != 0:
        print(f"You've entered wrong password. Your remaining right: {right}")
        right -= 1

    elif password != the_card.get("card-password") and right == 0:
        print("""You've entered your password incorrectly 3 times. 
        Please apply to the nearest X Bank branch office!""")

        exit()


if action_select == "1":
    print("""Your account balance is {} Dollars""".
    format(the_card.get("account-balance")))

elif action_select == "2":
    print("""Your account debt is {} Dollars. Deadline to pay off your debt is {}""".
    format(the_card.get("account-debt"), the_card.get("account-debt-deadline")))

elif action_select == "3":
    amount_1 = int(input("Please enter amount the you want to get withdraw: "))
    
    if int(the_card.get("account-balance")) < int(amount_1):
        print("INSUFFICIENT BALANCE!")
    
    else:
        print("Please check your money and take it.")
        new_amount = int(the_card.get("account-balance")) - int(amount_1)
        print(f"Your new account balance is {int(new_amount)} Dollars")

elif action_select == "4":
    amount_2 = int(input("Please enter amount the you want to get deposit: "))
    print("We've got your deposit.")
    new_amount_2 = int(the_card.get("account-balance")) + int(amount_2)
    print(f"Your new account balance is {int(new_amount_2)} Dollars")

elif action_select == "q" or action_select == "Q":
    print("Thank you and have a good day :)")
    exit()

else:
    print("Please enter correctly!")