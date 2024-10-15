import unittest
from block_004_GET_POST.flask_wtform import app


class RegistrationFormTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_missing_email(self):
        # Создаем POST запрос без email
        response = self.client.post('/registration', data={
            'phone': '1234567890',
            'name': 'John Doe',
            'address': '123 Elm Street'
        })
        self.assertEqual(response.status_code, 404)
        # Декодируем байты в строку и проверяем через f-строку
        response_text = response.data.decode("utf-8")
        self.assertIn(f"'email': ['This field is required.']", response_text)

    def test_missing_phone(self):
        # Создаем POST запрос без phone
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'name': 'John Doe',
            'address': '123 Elm Street'
        })
        self.assertEqual(response.status_code, 404)
        response_text = response.data.decode("utf-8")
        self.assertIn(f"'phone': ['This field is required.']", response_text)

    def test_missing_name(self):
        # Создаем POST запрос без name
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': '1234567890',
            'address': '123 Elm Street'
        })
        self.assertEqual(response.status_code, 404)
        response_text = response.data.decode("utf-8")
        self.assertIn(f"'name': ['This field is required.']", response_text)

    def test_missing_address(self):
        # Создаем POST запрос без address
        response = self.client.post('/registration', data={
            'email': 'test@example.com',
            'phone': '1234567890',
            'name': 'John Doe'
        })
        self.assertEqual(response.status_code, 404)
        response_text = response.data.decode("utf-8")
        self.assertIn(f"'address': ['This field is required.']", response_text)


if __name__ == '__main__':
    unittest.main()

