class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Mali", 100)
    account.deposit(50)
    print(f"{account.owner}'s balance: {account.get_balance()} baht")
