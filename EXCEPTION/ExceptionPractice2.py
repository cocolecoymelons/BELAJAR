
class NegativeAmountError(Exception):
        pass
class InsufficientBalanceError(Exception):
    pass
class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print("Deposit success")

    def withdraw(self,amount):
        self.balance -= amount
        print("Withdraw success")

    def show_balance(self):
        return self.balance

bank = Bank()
program_running = True
print("Welcome back, what we gonna do today?")
while program_running:

    choice = input(("\n1.Deposit\n2.Withdraw\n3.Show my balance\n0.Exit\n"))

    try:
        

        if choice == "1":
            amount = int(input("Please insert the amount:\n"))
            if amount <= 0:
                raise NegativeAmountError("Please input a number that is greater than 0!")
            bank.deposit(amount)

        elif choice == "2":
            amount = int(input("Please insert the amount:\n"))
            if amount <= 0:
                raise NegativeAmountError("Please input a number that is greater than 0!") 
            elif amount >= bank.balance:
                raise InsufficientBalanceError("Insufficient balance!")
            bank.withdraw(amount)
        elif choice == "3":
            print(f"Your balance: {bank.balance}$")
            
        elif choice == "0":
            print("See you later!")
            break
        else:
            print("Invalid menu")
    except ValueError as e:
        print(e)
    except InsufficientBalanceError as e:
        print(e)
    except NegativeAmountError as e:
         print(e)
            
        
        

