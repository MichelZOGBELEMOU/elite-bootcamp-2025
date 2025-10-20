"""A python script that modelise a class BankAccount and then initialize it"""
class BankAccount:
    """A simple class representing a Bank account"""
    def __init__(self, owner: str, balance: float=0.0):
        """Methods to Initialize BankAccount class"""
        # Validation of the arguments
        if not isinstance(balance, (float, int)):
            raise ValueError("The balance must be a number.")
        if balance < 0:
            raise ValueError("The balance must be a positive number.")

        #Initialisation of attributes
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self)->float:
        """A getter methode"""
        return self.__balance

    @balance.setter
    def balance(self, amount: float)-> None:
        if not isinstance(amount, (float, int)):
            raise ValueError("The balance must be a number")
        if amount < 0:
            raise ValueError("The balance must be positive")
        self.__balance = amount

    def deposit(self, amount: float):
        """Method to compute a deposit"""
        if not isinstance(amount, (float, int)):
            raise ValueError("The amount must be a number")
        if amount <= 0:
            raise ValueError("The amount must be positive.")
        
        self.balance += amount

    def withdraw(self, amount: float):
        """Method to execute a withdraw"""
        if amount > self.balance:
            raise ValueError("Insufficiant funds")
        if amount <= 0:
            raise ValueError("The withdraw amount must be positive")
        if not isinstance(amount, (float, int)):
            raise ValueError("The withdraw amount must be a number")
        self.balance -= amount

    def __repr__(self) -> str:
        """A method to display the owner and the balance of a bank account"""
        return f"Account Owner: {self.owner} -> Balance: ${self.balance:.2f}"

    def display_balance(self) -> str:
        """print a bank account"""
        return f"The balance is ${self.balance}"


def main():
    """The Program entry point"""
    my_bank_account = BankAccount("Michel Zogbelemou", 10000000)
    print(my_bank_account)
    my_bank_account.deposit(200000)
    print(my_bank_account)
    my_bank_account.withdraw(20000)
    print(my_bank_account.display_balance())


if __name__ == "__main__":
    main()
