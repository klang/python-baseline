from url_signer import get_url
import unittest
import requests

class TestUrlSigner(unittest.TestCase):

    def test_get_url(self):
        self.assertEqual(get_url("http://127.0.0.1:5000").text, "signed")

    def test_get_url_exception(self):
        self.assertRaises(requests.exceptions.HTTPError, get_url, "http://127.0.0.1:5000/nothing")

    def test_get_signed_url(self):
        self.assertEqual(get_url("http://127.0.0.1:5000").text, "signed")

    def test_get_signed_url_insist(self):
        self.assertEqual(get_url("http://127.0.0.1:5000").text, "signed")

# adding these two lines, will reduce cover to 90% when run from inside IntelliJ, but increase it to 100% when run from
# the command line.
if __name__ == "__main__":
    unittest.main()
