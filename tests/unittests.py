# These tests can be run using the unittest module in Python, and they cover various scenarios, such as valid and invalid input, future dates, and different birthday messages.These are examples and depending on the specific implementation of the solution, additional tests may be necessary to cover all possible edge cases.

import unittest
import requests

class TestHelloWorld(unittest.TestCase):

    def test_put_valid_username(self):
        # Test PUT request with valid username and dateOfBirth
        response = requests.put("http://localhost:8080/hello/Jane", json={"dateOfBirth": "2000-01-01"})
        self.assertEqual(response.status_code, 204)

    def test_put_invalid_username(self):
        # Test PUT request with invalid username (contains numbers)
        response = requests.put("http://localhost:8080/hello/Jane123", json={"dateOfBirth": "2000-01-01"})
        self.assertEqual(response.status_code, 400)

    def test_put_future_date(self):
        # Test PUT request with future dateOfBirth
        response = requests.put("http://localhost:8080/hello/Jane", json={"dateOfBirth": "2024-01-01"})
        self.assertEqual(response.status_code, 400)

    def test_get_birthday_today(self):
        # Test GET request with birthday today
        response = requests.get("http://localhost:8080/hello/Jane")
        expected_response = {"message": "Hello, Jane! Happy birthday!"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_get_birthday_in_5_days(self):
        # Test GET request with birthday in 5 days
        response = requests.get("http://localhost:8080/hello/Jane")
        expected_response = {"message": "Hello, Jane! Your birthday is in 5 day(s)"}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

if __name__ == '__main__':
    unittest.main()


