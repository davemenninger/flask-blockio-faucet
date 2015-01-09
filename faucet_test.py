import faucet
import unittest
import re

class FacuetTestCase(unittest.TestCase):

    def setUp(self):
        self.app = faucet.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        assert 'Home' in rv.data

    def test_balance(self):
        rv = self.app.get('/')
        assert 'doge balance is' in rv.data

    def test_dontation_address(self):
       rv = self.app.get('/')
       DOGEREGEX = re.compile('[1-9A-HJ-NP-Za-km-z]{34}')
       assert DOGEREGEX.search(rv.data)

if __name__ == '__main__':
   unittest.main()
