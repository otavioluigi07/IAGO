import unittest
from src.backend.services.modelService import ModelService

class TestModelService(unittest.TestCase):

    def test_create_model(self):
        # Testa a criação de um modelo
        result = ModelService.create_model(
            name="Modelo A",
            max_token="1000",
            min_token=True
        )
        self.assertIn('message', result)

    def test_get_model(self):
        # Testa a obtenção de um modelo existente
        result = ModelService.get_model(1)
        self.assertIn('id', result)

        # Testa a obtenção de um modelo que não existe
        result = ModelService.get_model(999)
        self.assertIn('error', result)

    def test_update_model(self):
        # Testa a atualização de um modelo existente
        result = ModelService.update_model(1, max_token="1500")
        self.assertIn('message', result)

        # Testa a atualização de um modelo que não existe
        result = ModelService.update_model(999, max_token="1500")
        self.assertIn('error', result)

    def test_delete_model(self):
        # Testa a exclusão de um modelo existente
        result = ModelService.delete_model(1)
        self.assertIn('message', result)

        # Testa a exclusão de um modelo que não existe
        result = ModelService.delete_model(999)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
