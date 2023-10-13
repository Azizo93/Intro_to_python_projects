pin_number = 1234
balance = 10000
attempts = 3
max_attempts = 0

while attempts > max_attempts:
    input_pin_number = int(input("Welcome to the Cash Machine! Please enter your PIN to begin: "))
    attempts -= 1
    if input_pin_number != pin_number:
        print("Wrong PIN")
        print(f"You have {attempts} attempts remaining")
    
    if attempts == 0: #ERROR! if pin is entered correct on third attempt it still prints below message, WHY?
        print("Sorry we are unable to process your request, please contact your provider.")
        
    elif input_pin_number == pin_number:
        print("Correct PIN, you may proceed") 
        print(f"Your balance is £{balance}.")
        
        withdrawal = float(input("How much would you like to withdraw today?: "))
        
        if balance > withdrawal:
            balance -= withdrawal
            print(f"Withdrawal complete. Your new balance is £{balance}.")
            break
        else:
            print(f"insuffient funds to complete transaction, please enter a lower amount.") 

        withdrawal = float(input("How much would you like to withdraw today?: ")) 
            
        if balance > withdrawal:
            balance -= withdrawal
            print(f"Withdrawal complete, Your new balance is £{balance}.")
        else:
            print(f"The amount requested is below your available balance: £{balance}. Please contact your nearest branch or try again later.")
    break 

print("Thank you, we hope to see you again!")     
        

        
    

    
        




    









