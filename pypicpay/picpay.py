from decimal import Decimal

import requests


class PicPay(object):

    __URL = "https://appws.picpay.com/ecommerce/public/"

    def __init__(self, x_picpay_token: str, x_seller_token: str):
        self.__x_picpay_token = x_picpay_token
        self.__x_seller_token = x_seller_token

    @property
    def _x_picpay_token(self):
        """The _x_picpay_token

        Returns:
            _type_: The _x_picpay_token
        """
        return self.__x_picpay_token

    @property
    def _x_seller_token(self):
        """The _x_seller_token

        Returns:
            _type_: The _x_seller_token
        """
        return self.__x_seller_token

    @property
    def url(self):
        """The base url

        Returns:
            _type_: the base url
        """
        return self.__URL

    def _get_full_url(self, path: str) -> str:
        """Return the full url

        Args:
            path (str): path of url

        Returns:
            str: The full url
        """
        return f"{self.url}{path}"

    @property
    def headers(self) -> dict:
        """Formata os headers de autenticação da requisição.

        Returns:
            dict: Headers de autenticação.
        """
        return {
            "x-picpay-token": self._x_picpay_token,
            "x-seller-token": self._x_seller_token,
        }

    def _request(self, method: str, path: str, json: dict, **kwargs):
        """Realiza uma requisição HTTP.

        Args:
            method (str): Método http.
            path (str): Caminho da requisição.
            json (dict): Dados da requisição.

        Returns:
            [type]: O retorno da requisição.
        """
        request = requests.request(
            method=method,
            url=self._get_full_url(path),
            headers=self.headers,
            json=json,
            **kwargs,
        )
        json = request.json()
        return json

    def payment(
        self,
        reference_id: str,
        callback_url: str,
        value: Decimal,
        buyer: dict,
        return_url: str = None,
        expires_at: str = None,
    ) -> dict:
        """Seu e-commerce irá solicitar o pagamento de um pedido através do PicPay na finalização do carrinho de compras.
        Após a requisição http, o cliente deverá ser redirecionado para o endereço informada no campo paymentUrl para que o mesmo possa finalizar o pagamento.

        Assim que o pagamento for concluído o cliente será redirecionado para o endereço informada no campo returnUrl do json enviado pelo seu e-commerce
        no momento da requisição. Se não informado, nada acontecerá (o cliente permanecerá em nossa página de checkout).

        Caso seja identificado que seu cliente também é cliente PicPay, iremos enviar um push notification e uma notificação dentro do aplicativo PicPay
        avisando sobre o pagamento pendente. Para todos os casos iremos enviar um e-mail de pagamento pendente contendo o link de nossa página de checkout.

        Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Requisicao-de-Pagamento

        Args:
            reference_id (str): Identificador único do ecommerce.
            callback_url (str): Endereço de callback do ecommerce para notificações.
            value (Decimal): Valor do pedido.
            buyer (dict): Dados do comprador.
            return_url (str, optional): . Endereço do pedido no ecommerce.
            expires_at (str, optional): Data de expiração do pagamento.

        Returns:
            dict: Dados do pagamento.
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

    def cancellation(
        self, reference_id: str, authorization_id: str = None
    ) -> dict:
        """Utilize este endereço para solicitar o cancelamento/estorno de um pedido. Valem as seguintes regras:

        a) Se já foi pago, o cliente PicPay será estornado caso sua conta de Lojista no PicPay tenha saldo para
        realizar o estorno e caso o cliente PicPay tenha recebido algum cashback nesta transação, este valor será estornado do cliente
        (para isto o mesmo deve possuir saldo). Além disso, é nescessário o ID de autorização, conforme a documentação do PicPay. Todas
        esses requisitos devem ser cumpridos para que o estorno da transação ocorra com sucesso.

        b) Se ainda não foi pago, a transação será cancelada em nosso servidor e não permitirá pagamento por parte do cliente PicPay;

        Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Cancelamento

        Args:
            reference_id (str): Identificador único do ecommerce.
            authorization_id (str, optional): ID de autorização equivalente ao pagamento.

        Returns:
            dict: Dados do cancelamento.
        """
        path = f"payments/{reference_id}/cancellations"

        json = {
            "referenceId": reference_id,
        }

        if authorization_id:
            json["authorization_id"] = authorization_id

        request = self._request(method="post", path=path, json=json)

        return request

    def status(self, reference_id: str) -> dict:
        """Utilize o endpoint (requisição GET) abaixo para consultar o status de sua requisição de pagameto.

        Saiba mais em: https://ecommerce.picpay.com/doc/#operation/getStatus

        Args:
            reference_id (str): Identificador único do ecommerce.

        Returns:
            dict: Dados do status.
        """
        path = f"payments/{reference_id}/status"

        json = {
            "referenceId": reference_id,
        }

        request = self._request(method="get", path=path, json=json)

        return request

    def notification(self, reference_id: str) -> dict:
        """Iremos notificar o callbackUrl (fornecido na requisição de pagamento), via método POST, informando que houve uma alteração no status do pedido.

        Porém, por questões de segurança, não iremos informar o novo status nesta requisição.
        Para isto, sua loja (a partir do recebimento de nossa notificação) deverá consultar nosso endpoint de status de pedidos.

        Para que o callback seja considerado confirmado, sua loja deve responder com HTTP Status 200.

        Saiba mais em: https://ecommerce.picpay.com/doc/#operation/postCallbacks

        Args:
            reference_id (str): Identificador único do ecommerce.

        Returns:
            dict: Dados da notificação.
        """
        path = "callback"

        json = {"referenceId": reference_id}
        request = self._request(method="post", path=path, json=json)

        return request
