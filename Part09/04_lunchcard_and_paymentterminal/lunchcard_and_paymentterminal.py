# WRITE YOUR SOLUTION HERE:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        cost = 2.50
        if payment < cost:
            return payment
        else:
            self.funds += cost
            self.lunches += 1
            payment_change = payment - cost
            return payment_change


    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        cost = 4.30
        if payment < cost:
            return payment
        else:
            self.funds += cost
            self.specials += 1
            payment_change = payment - cost
            return payment_change


    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        cost = 2.50
        if card.balance < cost:
            return False
        else:
            card.balance -= cost
            self.lunches += 1
            return True

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        cost = 4.30
        if card.balance < cost:
            return False
        else:
            card.balance -= cost
            self.specials += 1
            return True

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount < 0:
            raise ValueError("why are you putting less than 0 HUH ?? ")
        else:
            self.funds += amount
            card.balance += amount