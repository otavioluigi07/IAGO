import unittest
from src.backend.services.userService import UserService

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        # Testa a criação de um usuário
        result = UserService.create_user(
            name="Test User",
            email="test@example.com",
            occupation="Tester",
            cell="123456789",
            age="30",
            gender="Male",
            subscription_id=1,
            role="user"
        )
        self.assertIn('message', result)

    def test_get_user(self):
        # Testa a obtenção de um usuário existente
        result = UserService.get_user(1)
        self.assertIn('id', result)

        # Testa a obtenção de um usuário que não existe
        result = UserService.get_user(999)
        self.assertIn('error', result)

    def test_update_user(self):
        # Testa a atualização de um usuário existente
        result = UserService.update_user(1, occupation="Senior Tester")
        self.assertIn('message', result)

        # Testa a atualização de um usuário que não existe
        result = UserService.update_user(999, occupation="Senior Tester")
        self.assertIn('error', result)

    def test_delete_user(self):
        # Testa a exclusão de um usuário existente
        result = UserService.delete_user(1)
        self.assertIn('message', result)

        # Testa a exclusão de um usuário que não existe
        result = UserService.delete_user(999)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
