#instead of multiple if-else to check if payment is card then return CreditCardPayment and all others, we send the exact payment method and complete payment 

"""
You have one task.

But there are multiple ways to do it.

Example:

Payment → credit, paypal, applepay

Discount → student, premium, no-discount

Sorting → quicksort, mergesort, bubble sort

Without Strategy, we usually write:

if method == "credit":
    ...
elif method == "paypal":
    ...
elif method == "applepay":
    ...
"""

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)
        

strategy = PayPalPayment() # we direct send the exact payment method to our context
payment = PaymentContext(strategy)
payment.execute_payment(500)