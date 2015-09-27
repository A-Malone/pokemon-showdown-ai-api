import unittest
from showdown_client import ShowdownClient

class Login(unittest.TestCase):
    def setUp(self):
        self.client = ShowdownClient()
    def test_login(self):
        self.client.login('fear27', 'blurnfear')
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
