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

    def submit_address(self, address):
        return self.app.post('/', data=dict(address=address) )

    def test_addresses(self):
        rv = self.submit_address('foo')
        assert 'not good' in rv.data
        rv = self.submit_address('DH8EkHiwpzCmjm3R9sCcxdUqqgykmwR5f1')
        assert 'WOW' in rv.data


if __name__ == '__main__':
   unittest.main()
