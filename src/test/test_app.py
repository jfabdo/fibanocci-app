# import json
import unittest

from app import app


class TestUtilityApis(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fibonacci_bad_request(self):
        response = self.app.get('/fibonacci/-10')
        self.assertEqual(response.status_code, 400)
        response = self.app.get('/fibonacci/hey')
        self.assertEqual(response.status_code, 400)

    # def test_fibonacci_returns_first_number(self):
    #     response = self.app.get('/fibonacci/1')
    #     req_json = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(req_json["results"], [0])

    # def test_fibonacci_returns_first_two_numbers(self):
    #     response = self.app.get('/fibonacci/2')
    #     req_json = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(req_json["results"], [0, 1])

    # def test_fibonacci_returns_n_numbers(self):
    #     response = self.app.get('/fibonacci/5')
    #     req_json = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(req_json["results"], [0, 1, 1, 2, 3])
    #     response = self.app.get('/fibonacci/8')
    #     req_json = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(req_json["results"], [0, 1, 1, 2, 3, 5, 8, 13])

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World. Never do Live Demos')
