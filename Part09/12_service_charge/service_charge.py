class BankAccount:

    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("amount is less than 0")
        else:
            self.balance += amount
            self.balance -= self.__service_charge()

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough money in account")
        else:
            self.balance -= amount
            self.balance -= self.__service_charge()

    def balance(self):
        return self.balance

    def __service_charge(self):
        self.service_charge = self.balance * 0.01
        return self.service_charge