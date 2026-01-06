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

    def test_this_works(self):
        with self.assertRaises(UsernameException):
            raise UsernameException()


if __name__ == '__main__':
    unittest.main()
