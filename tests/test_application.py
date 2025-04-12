import unittest
from application import application
from funtions import load_file

class TestApplication(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = application.test_client()
        self.app.testing = True
        self.data = load_file('./heroes.csv')

    def test_index_route(self):
        # Test the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.data)

    def test_heroe_route_valid_id(self):
        # Test the /<id> route with a valid ID
        response = self.app.get('/0')  # ID 0 corresponds to A-Bomb
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.data['0'])

    def test_heroe_route_invalid_id(self):
        # Test the /<id> route with an invalid ID
        response = self.app.get('/999')  # Non-existent ID
        self.assertEqual(response.status_code, 500)  # Expecting server error

if __name__ == '__main__':
    unittest.main()