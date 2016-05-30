import unittest
from app.app import app

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)

class TillTestCase(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()
