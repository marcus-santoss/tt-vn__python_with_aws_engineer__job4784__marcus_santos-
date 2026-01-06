from src.exceptions import PaymentException
from src.models import User


class MiniVenmo:
    @staticmethod
    def create_user(username, balance, credit_card_number):
        user = User(username)
        user.add_credit_card(credit_card_number)
        user.add_to_balance(balance)
        return user

    @staticmethod
    def render_feed(feed):
        for message in feed:
            print(message)

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
        carol = venmo.create_user("Carol", 10.00, "4242424242424242")

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")

            # should complete using card
            carol.pay(bobby, 15.00, "Lunch")
        except PaymentException as e:
            print(e)

        # Add Bob's Friend
        bobby.add_friend(carol)

        # Getting Bob's Feed
        feed = bobby.retrieve_feed()

        # Render Feed
        venmo.render_feed(feed)


if __name__ == '__main__':
    MiniVenmo.run()
