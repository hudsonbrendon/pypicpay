from pypicpay import PicPay, __version__


def test_version():
    assert __version__ == "0.4.8"


class TestPicPay:
    def test_instance(self, picpay):
        assert isinstance(picpay, PicPay)

    def test_x_picpay_token(self, picpay):
        assert picpay._x_picpay_token == "test"

    def test_x_seller_token(self, picpay):
        assert picpay._x_seller_token == "test"

    def _get_full_url(self, picpay):
        assert picpay._get_full_url("/test") == f"{picpay._URL}/test"

    def test_headers(self, picpay):
        assert picpay.headers == {
            "x-picpay-token": picpay._x_picpay_token,
            "x-seller-token": picpay._x_seller_token,
        }

    def test_payment(self, requests_mock, picpay, payment_payload, buyer):
        url = picpay._get_full_url(path="payments")
        requests_mock.post(url=url, json=payment_payload)
        payment = picpay.payment(
            reference_id=102030,
            callback_url="https://www.sualoja.com.br/callback",
            return_url="https://www.sualoja.com.br/cliente/pedido/102030",
            value=20.50,
            expires_at="2022-05-01T16:00:00-03:00",
            buyer=buyer,
        )
        assert payment == payment_payload

    def test_cancellation(
        self, requests_mock, picpay, payment_cancellations_payload
    ):
        url = picpay._get_full_url(path="payments/102030/cancellations")
        requests_mock.post(url=url, json=payment_cancellations_payload)
        cancellation = picpay.cancellation(reference_id=102030)
        assert cancellation == payment_cancellations_payload

    def test_status(self, requests_mock, picpay, payment_status):
        url = picpay._get_full_url(path="payments/102030/status")
        requests_mock.get(url=url, json=payment_status)
        status = picpay.status(reference_id=102030)
        assert status == payment_status

    def test_notification(self, requests_mock, picpay):
        url = picpay._get_full_url(path="callback")
        requests_mock.post(url=url, json={})
        notification = picpay.notification(reference_id=102030)
        assert notification == {}
