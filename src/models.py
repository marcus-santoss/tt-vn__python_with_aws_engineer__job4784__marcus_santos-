import re
import uuid

from src.exceptions import UsernameException, CreditCardException, PaymentException


class Payment:

    def __init__(self, amount, actor, target, note):
        self.id = str(uuid.uuid4())
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note


class User:
    def __init__(self, username: str):
        if not self._is_valid_username(username):
            raise UsernameException('Username not valid.')

        self.username: str = username
        self.credit_card_number: str | None = None
        self.balance: float = 0.0
        self.feed: list[str] = []

    def retrieve_feed(self):
        return self.feed

    def add_friend(self, new_friend):
        # TODO: add code here
        pass

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException('Invalid credit card number.')

    def pay(self, target, amount, note) -> Payment:
        if self.balance <= amount:
            return self.pay_with_balance(target, amount, note)

        return self.pay_with_card(target, amount, note)

    def pay_with_card(self, target, amount, note) -> Payment:
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')

        elif amount <= 0.0:
            raise PaymentException('Amount must be a non-negative number.')

        elif self.credit_card_number is None:
            raise PaymentException('Must have a credit card to make a payment.')

        self._charge_credit_card(self.credit_card_number)
        target.add_to_balance(amount)
        payment = Payment(amount, self, target, note)
        self.add_feed(payment)

        return payment

    def add_feed(self, payment: Payment):
        msg = f"{self.username} paid {payment.target.username} ${payment.amount} for {payment.note}"
        self.feed.append(msg)

    def pay_with_balance(self, target: User, amount: float, note: str) -> Payment:
        # removes the balance from payer
        self.balance -= amount

        # Add the bance to the receiver
        target.add_to_balance(amount)

        # Store de history of transaction
        payment = Payment(amount, "Balance", target, note)
        self.add_feed(payment)

        return payment

    @staticmethod
    def _is_valid_credit_card(credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    @staticmethod
    def _is_valid_username(username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass
