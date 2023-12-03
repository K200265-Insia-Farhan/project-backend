# test_app.py

import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_endpoint(self):
        # Test the home endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello from Flask Backend!')

    def test_nonexistent_endpoint(self):
        # Test a non-existent endpoint
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_content_type(self):
        # Test the content type of the response
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)

    def test_index_route(self):
        # Test the behavior of the index route
        response = self.app.get('/')
        self.assertTrue(b'Hello' in response.data)

    def test_debug_mode(self):
        # Test if the application is NOT running in debug mode
        self.assertFalse(app.debug)

if __name__ == '__main__':
    unittest.main()
