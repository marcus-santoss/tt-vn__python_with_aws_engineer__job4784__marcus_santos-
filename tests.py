import unittest

from src.exceptions import UsernameException, CreditCardException
from src.models import User


class TestUser(unittest.TestCase):

    def test_create_new_user(self):
        username = "test"
        credit_card_number = "4111111111111111"
        balance = 100
        u = User(username)
        u.add_credit_card(credit_card_number)
        u.add_to_balance(balance)

        self.assertEqual(u.username, username)
        self.assertEqual(u.credit_card_number, credit_card_number)
        self.assertEqual(u.balance, balance)

    def test_create_user_with_invalid_credit_card_number(self):
        username = "test"
        credit_card_number = "1111111111111111"
        with self.assertRaises(CreditCardException):
            u = User(username)
            u.add_credit_card(credit_card_number)

    def test_create_user_with_invalid_username(self):
        username = "@Jack#Bottleneck"
        with self.assertRaises(UsernameException):
            User(username)

    def test_payment(self):
        u1 = User("test1")
        u1.add_credit_card("4111111111111111")
        u1.add_to_balance(10)

        u2 = User("test2")
        u2.add_credit_card("4242424242424242")
        u2.add_to_balance(10)

        u1.pay(u2, 5, "Coffe")

        print(u1.balance)
        print(u2.balance)
        self.assertEqual(u1.balance, 5)
        self.assertEqual(u2.balance, 15)


if __name__ == '__main__':
    unittest.main()
