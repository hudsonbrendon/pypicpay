import unittest
import requests_mock

from picpay import PicPay
from decouple import config


class TestPicPay(unittest.TestCase):
    def setUp(self):
        self.picpay = PicPay(
            x_picpay_token=config("X_PICPAY_TOKEN"),
            x_seller_token=config("X_SELLER_TOKEN"),
        )

    def test_get_url(self):
        self.assertEqual(self.picpay._get_url("/test"), f"{self.picpay._URL}/test")


if __name__ == "__main__":
    unittest.main()
