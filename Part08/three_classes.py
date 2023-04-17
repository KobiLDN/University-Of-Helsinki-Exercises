# Write your solution here
class Checklist:

    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:

    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:

    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


class BankAccount:

    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

    # this function creates a new bank account object and returns it

if __name__ == "__main__":

    def open_account(name: str):
        new_account = BankAccount(0, name)
        return new_account


    # this function adds the amount passed as an argument to the balance of the bank account also passed as an argument
    def deposit_money_on_account(account: BankAccount, amount: int):
        account.balance += amount


    peters_account = open_account("Peter Python")
    print(peters_account.balance)

    deposit_money_on_account(peters_account, 500)

    print(peters_account.balance)
