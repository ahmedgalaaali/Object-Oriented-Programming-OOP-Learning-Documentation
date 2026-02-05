class Account:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self._balance = balance
    @property
    def get_id(self):
        return self.__id
    @property
    def get_name(self):
        return self.__name
    @property
    def balance(self):
        agreement = str(input("Showing your balance will charge you 0.25$. Agree (Y), disagree (N)."))
        if agreement == "Y":
            if self._balance >= 0.25:
                self._balance -= 0.25
                print(f"Your balance is: {self._balance}$")
            else: print("Insuffecient fund.")
        elif agreement == "N":
            print(f"Operation cancelled.")

    def withdraw(self, amount):
        self._balance -= amount
        print(f"Withdrew ${amount}. New Balance: ${self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. New Balance: ${self._balance}")

class Saving(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Transaction Denied: Insufficient Funds!")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount} from Savings. Remaining: ${self._balance}")

class Checking(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Overdraft Warning: Applying $10 Fee.")
            self._balance -= (amount + 10)
        else:
            self._balance -= amount
        print(f"Withdrew ${amount} (Checking). Remaining: ${self._balance}")
