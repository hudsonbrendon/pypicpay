import unittest

import requests_mock
from picpay import PicPay


class TestPicPay(unittest.TestCase):
    def setUp(self):
        self.picpay = PicPay(
            x_picpay_token="x_picpay_token", x_seller_token="x_seller_token",
        )

    def test_get_url(self):
        self.assertEqual(self.picpay._get_url("/test"), f"{self.picpay._URL}/test")

    def test_headers(self):
        self.assertEqual(
            self.picpay.headers,
            {
                "x-picpay-token": self.picpay._x_picpay_token,
                "x-seller-token": self.picpay._x_seller_token,
            },
        )

    @requests_mock.Mocker()
    def test_payment(self, request_mock):
        url = self.picpay._get_url(path="payments")
        json = {
            "referenceId": "102030",
            "paymentUrl": "https://app.picpay.com/checkout/NWUzM2IwYjNiM2U0YmI0M2U5Njk1NjAy",
            "qrcode": {
                "content": "https://app.picpay.com/checkout/NWUzM2IwYjNiM2U0YmI0M2U5Njk1NjAy",
                "base64": "data:image/png;base64,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",
            },
            "expiresAt": "2022-05-01T16:00:00-03:00",
        }
        request_mock.post(url=url, json=json)
        payment = self.picpay.payment(
            reference_id=102030,
            callback_url="http://www.sualoja.com.br/callback",
            return_url="http://www.sualoja.com.br/cliente/pedido/102030",
            value=20.50,
            expires_at="2022-05-01T16:00:00-03:00",
            buyer={
                "firstName": "João",
                "lastName": "Da Silva",
                "document": "123.456.789-10",
                "email": "teste@picpay.com",
                "phone": "+55 27 12345-6789",
            },
        )
        self.assertEqual(payment, json)

    @requests_mock.Mocker()
    def test_cancellation(self, request_mock):
        url = self.picpay._get_url(path="payments/102030/cancellations")
        json = {"referenceId": "102030", "cancellationId": "5e34e3415385626b6d18f25c"}
        request_mock.post(url=url, json=json)
        cancellation = self.picpay.cancellation(reference_id=102030)
        self.assertEqual(cancellation, json)

    @requests_mock.Mocker()
    def test_status(self, request_mock):
        url = self.picpay._get_url(path="payments/102030/status")
        json = {"referenceId": "102030", "status": "expired"}
        request_mock.get(url=url, json=json)
        status = self.picpay.status(reference_id=102030)
        self.assertEqual(status, json)

    @requests_mock.Mocker()
    def test_notification(self, request_mock):
        url = self.picpay._get_url(path="callback")
        json = {}
        request_mock.post(url=url, json=json)
        notification = self.picpay.notification(reference_id=102030)
        self.assertEqual(notification, json)


if __name__ == "__main__":
    unittest.main()
