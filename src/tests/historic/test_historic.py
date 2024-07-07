import unittest
from src.backend.services.historicService import HistoricService

class TestHistoricService(unittest.TestCase):

    def test_create_purchase_history(self):
        # Testa a criação de um registro no histórico de compras
        result = HistoricService.create_purchase_history(
            user_id=1,
            subscription_id=1,
            total_price=19.99,
            payment_method="credit_card",
            status=True
        )
        self.assertIn('message', result)

    def test_get_purchase_history(self):
        # Testa a obtenção de um registro no histórico de compras existente
        result = HistoricService.get_purchase_history(1)
        self.assertIn('id', result)

        # Testa a obtenção de um registro no histórico de compras que não existe
        result = HistoricService.get_purchase_history(999)
        self.assertIn('error', result)

    def test_update_purchase_history(self):
        # Testa a atualização de um registro no histórico de compras existente
        result = HistoricService.update_purchase_history(1, total_price=24.99)
        self.assertIn('message', result)

        # Testa a atualização de um registro no histórico de compras que não existe
        result = HistoricService.update_purchase_history(999, total_price=24.99)
        self.assertIn('error', result)

    def test_delete_purchase_history(self):
        # Testa a exclusão de um registro no histórico de compras existente
        result = HistoricService.delete_purchase_history(1)
        self.assertIn('message', result)

        # Testa a exclusão de um registro no histórico de compras que não existe
        result = HistoricService.delete_purchase_history(999)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
