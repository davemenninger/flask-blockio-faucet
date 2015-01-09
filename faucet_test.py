import faucet
import unittest

class FacuetTestCase(unittest.TestCase):

    def setUp(self):
        self.app = faucet.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def test_balance(self):
        rv = self.app.get('/')
        assert 'doge balance is' in rv.data

if __name__ == '__main__':
   unittest.main()
