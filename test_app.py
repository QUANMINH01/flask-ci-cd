import unittest
from app import app

class HelloRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_route(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello CI/CD")

if __name__ == '__main__':
    unittest.main()
