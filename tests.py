import unittest

from src.exceptions import UsernameException, CreditCardException, PaymentException
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

        self.assertEqual(u1.balance, 5)
        self.assertEqual(u2.balance, 15)

    def test_payment_with_card(self):
        u1 = User("test1")
        u1.add_credit_card("4111111111111111")
        u1.add_to_balance(10)

        u2 = User("test2")
        u2.add_credit_card("4242424242424242")
        u2.add_to_balance(10)

        u1.pay(u2, 20, "Coffe")

        print(u1.balance)
        print(u2.balance)
        self.assertEqual(u1.balance, 10)
        self.assertEqual(u2.balance, 30)

    def test_payment_without_card(self):
        u1 = User("test1")
        u1.add_to_balance(10)

        u2 = User("test2")
        u2.add_credit_card("4242424242424242")
        u2.add_to_balance(10)

        with self.assertRaises(PaymentException):
            u1.pay(u2, 20, "Coffe")

    def test_add_friend(self):
        u1 = User("test1")
        u2 = User("test2")

        u1.add_friend(u2)
        self.assertEqual(u1.friends, [u2])

    def test_add_two_friends(self):
        u1 = User("test1")
        u2 = User("test2")
        u3 = User("test3")

        u1.add_friend(u2)
        u1.add_friend(u3)
        self.assertEqual(u1.friends, [u2, u3])

    def test_add_friend_twice(self):
        u1 = User("test1")
        u2 = User("test2")

        u1.add_friend(u2)
        self.assertEqual(u1.friends, [u2])
        self.assertEqual(1, len(u1.friends))


if __name__ == '__main__':
    unittest.main()
