# MINI BANK SYSTEM
NAME="PRANAY20061002"
EXIT=4
class BankAccount:
    LIMIT=10000
    def __init__(self,account_name,init_money):
        self.init_money=init_money
        self.account_name=account_name
    def withdraw(self,amount):
        if amount>self.init_money:
            raise ValueError("Insuffcient Balance")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount>self.LIMIT:
            raise OverflowError(f"Cannot withdraw greater than {self.LIMIT}")
        self.init_money-=amount
        

    def deposit(self,amount):
        if amount>self.LIMIT:
            raise OverflowError(f"Cannot deposit greater than {self.LIMIT} at a time")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.init_money+=amount

    def check_balance(self):
        return self.init_money


def main():
    
    try:
        balance=int(input("Enter the inital amount in your account: "))
        if balance<0:
            raise ValueError("inital balance can't be negative..")
        Account=BankAccount(NAME,balance)
    except ValueError as e:
        print(e)
        return
    
    
        
    while True:

        print("---------------OPTIONS-----------------")
        print("\n1 for withdrawing money\n2 for depositing money\n3 for checking balance\n4 for exiting...")
        try:
            option=int(input("Enter the option: "))
            if option==1:
                amount=int(input("Enter the amount you want to wthdraw: "))
                Account.withdraw(amount)
            elif option==2:
                amount=int(input("Enter the amount you want to deposit: "))
                Account.deposit(amount)
            elif option==3:
                money=Account.check_balance()
                print(f"BALANCE={money}")

            elif option==EXIT:
                print("Exiting...!")
                break
            else:
                raise ValueError("Please enter from the given options...")
        except ValueError as e:
            print(e)
            continue
        except OverflowError as e:
            print(e)
            continue


main()