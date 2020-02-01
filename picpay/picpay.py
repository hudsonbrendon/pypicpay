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

    def cancellation(self, reference_id):
        """
        Utilize este endereço para solicitar o cancelamento/estorno de um pedido. Valem as seguintes regras:
        
        a) Se já foi pago, o cliente PicPay será estornado caso sua conta de Lojista no PicPay tenha saldo para
        realizar o estorno e caso o cliente PicPay tenha recebido algum cashback nesta transação, este valor será estornado do cliente
        (para isto o mesmo deve possuir saldo). Todas esses requisitos devem ser cumpridos para que o estorno da transação ocorra com sucesso.
        
        b) Se ainda não foi pago, a transação será cancelada em nosso servidor e não permitirá pagamento por parte do cliente PicPay;

        Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Cancelamento
        """
        path = f"payments/{reference_id}/cancellations"

        json = {
            "referenceId": reference_id,
        }

        request = self._request(method="post", path=path, json=json)

        return request

    def status(self, reference_id):
        """
        Utilize o endpoint (requisição GET) abaixo para consultar o status de sua requisição de pagameto.

        Saiba mais em: https://ecommerce.picpay.com/doc/#operation/getStatus
        """
        path = f"payments/{reference_id}/status"

        json = {
            "referenceId": reference_id,
        }

        request = self._request(method="get", path=path, json=json)

        return request

    def notification(self, reference_id):
        """
        Iremos notificar o callbackUrl (fornecido na requisição de pagamento), via método POST, informando que houve uma alteração no status do pedido.

        Porém, por questões de segurança, não iremos informar o novo status nesta requisição.
        Para isto, sua loja (a partir do recebimento de nossa notificação) deverá consultar nosso endpoint de status de pedidos.

        Para que o callback seja considerado confirmado, sua loja deve responder com HTTP Status 200.
        
        Saiba mais em: https://ecommerce.picpay.com/doc/#operation/postCallbacks
        """
        path = "callback"

        json = {"referenceId": reference_id}
        request = self._request(method="post", path=path, json=json)

        return request
