#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, total, quantity=1):
        self.title = title
        self.total += total * quantity
        for i in range(quantity):
            self.items.append(title)
        self.last_transaction = total * quantity

    def apply_discount(self):
        if self.discount > 1:
            self.total = self.total - int((self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
