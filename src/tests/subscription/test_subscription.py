import unittest
from src.backend.services.subscriptionService import SubscriptionService

class TestSubscriptionService(unittest.TestCase):

    def test_create_subscription(self):
        # Testa a criação de uma subscrição
        result = SubscriptionService.create_subscription(
            name="Premium",
            price="19.99",
            model="monthly",
            active=True
        )
        self.assertIn('message', result)

    def test_get_subscription(self):
        # Testa a obtenção de uma subscrição existente
        result = SubscriptionService.get_subscription(1)
        self.assertIn('id', result)

        # Testa a obtenção de uma subscrição que não existe
        result = SubscriptionService.get_subscription(999)
        self.assertIn('error', result)

    def test_update_subscription(self):
        # Testa a atualização de uma subscrição existente
        result = SubscriptionService.update_subscription(1, price="24.99")
        self.assertIn('message', result)

        # Testa a atualização de uma subscrição que não existe
        result = SubscriptionService.update_subscription(999, price="24.99")
        self.assertIn('error', result)

    def test_delete_subscription(self):
        # Testa a exclusão de uma subscrição existente
        result = SubscriptionService.delete_subscription(1)
        self.assertIn('message', result)

        # Testa a exclusão de uma subscrição que não existe
        result = SubscriptionService.delete_subscription(999)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
