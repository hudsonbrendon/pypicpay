import requests


class PicPay(object):

    _URL = "https://appws.picpay.com/ecommerce/public/"

    def __init__(self, x_picpay_token, x_seller_token):
        self._x_picpay_token = x_picpay_token
        self._x_seller_token = x_seller_token

    def _get_url(self, path):
        return f"{self._URL}{path}"

    @property
    def headers(self):
        return {
            "x-picpay-token": self._x_picpay_token,
            "x-seller-token": self._x_seller_token,
        }

    def _request(self, method, path, json, **kwargs):
        request = requests.request(
            method=method,
            url=self._get_url(path),
            headers=self.headers,
            json=json,
            **kwargs,
        )
        json = request.json()
        return json

    def payment(
        self, reference_id, callback_url, value, buyer, return_url=None, expires_at=None
    ):
        """
        Seu e-commerce irá solicitar o pagamento de um pedido através do PicPay na finalização do carrinho de compras.
        Após a requisição http, o cliente deverá ser redirecionado para o endereço informada no campo paymentUrl para que o mesmo possa finalizar o pagamento.

        Assim que o pagamento for concluído o cliente será redirecionado para o endereço informada no campo returnUrl do json enviado pelo seu e-commerce no momento da requisição.
        Se não informado, nada acontecerá (o cliente permanecerá em nossa página de checkout).

        Caso seja identificado que seu cliente também é cliente PicPay, iremos enviar um push notification e uma notificação dentro do aplicativo PicPay avisando sobre o pagamento pendente.
        Para todos os casos iremos enviar um e-mail de pagamento pendente contendo o link de nossa página de checkout.

        Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Requisicao-de-Pagamento
        """
        path = "payments"

        json = {
            "referenceId": reference_id,
            "callbackUrl": callback_url,
            "returnUrl": return_url,
            "value": value,
            "expiresAt": expires_at,
            "buyer": buyer,
        }

        request = self._request(method="post", path=path, json=json)

        return request
