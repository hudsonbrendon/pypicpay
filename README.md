# PicPay Python

Aceite PicPay e faça parte do movimento que está revolucionando a relação com o dinheiro no Brasil.

![Python package](https://github.com/hudsonbrendon/picpay-python/workflows/Python%20package/badge.svg?branch=master)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/picpay-python.svg?style=flat)](https://github.com/hudsonbrendon/picpay-python/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![PicPay](logo.png)

# Recursos Disponíveis

- [x]  Requisição de Pagamento
- [x]  Cancelamento
- [x]  Status
- [x]  Notificação

# Instalação

```bash
$ pip install picpay-python
```
ou

```bash
$ python setup.py install
```

# Modo de usar

Todas as APIs do PicPay Developers foram desenvolvidas baseadas na tecnologia REST, seguindo os atuais padrões técnicos de mercado. Tudo isso para que a experiência na hora da integração seja a mais fácil possível. Todas as URLs são amigáveis e orientadas a recursos e utilizam os padrões do protocolo HTTP como autenticação, verbos e códigos de retorno. Isso permite que APIs possam ser utilizadas por clientes HTTP já existentes. Todas as respostas são retornadas no formato JSON.

Como pode ser visto abaixo, as APIs foram cuidadosamente trabalhadas para que os termos de negócios contidos sejam facilmente entendidos por desenvolvedores que não tenham conhecimento prévio do sistema. Elas foram meticulosamente estudadas para que um nome de campo em um endpoint tenha rigorosamente o mesmo significado em outros recursos.

Atenção: Todos os testes devem ser realizados em produção sem ônus ao desenvolvedor: todos os pagamentos realizados podem ser imediatamente estornados (tanto pela API quanto pelo painel do lojista).

Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Introducao

## Requisição de Pagamento

Seu e-commerce irá solicitar o pagamento de um pedido através do PicPay na finalização do carrinho de compras. Após a requisição http, o cliente deverá ser redirecionado para o endereço informada no campo paymentUrl para que o mesmo possa finalizar o pagamento.

Assim que o pagamento for concluído o cliente será redirecionado para o endereço informada no campo returnUrl do json enviado pelo seu e-commerce no momento da requisição. Se não informado, nada acontecerá (o cliente permanecerá em nossa página de checkout).

Caso seja identificado que seu cliente também é cliente PicPay, iremos enviar um push notification e uma notificação dentro do aplicativo PicPay avisando sobre o pagamento pendente. Para todos os casos iremos enviar um e-mail de pagamento pendente contendo o link de nossa página de checkout.

Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Requisicao-de-Pagamento

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

payment = picpay.payment(
    reference_id=102030,
    callback_url="https://picpay.com/site",
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
```

## Cancelamento

Utilize este método para solicitar o cancelamento/estorno de um pedido. Valem as seguintes regras:

a) Se já foi pago, o cliente PicPay será estornado caso sua conta de Lojista no PicPay tenha saldo para realizar o estorno e caso o cliente PicPay tenha recebido algum cashback nesta transação, este valor será estornado do cliente (para isto o mesmo deve possuir saldo). Todas esses requisitos devem ser cumpridos para que o estorno da transação ocorra com sucesso.

b) Se ainda não foi pago, a transação será cancelada em nosso servidor e não permitirá pagamento por parte do cliente PicPay;

Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Cancelamento

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

cancellation = picpay.cancellation(reference_id=102030)
```

## Status

Utilize este método para solicitar o status de um pedido.

Saiba mais em: https://ecommerce.picpay.com/doc/#operation/getStatus

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

status = picpay.status(reference_id=102030)
```

## Notificação

Iremos enviar uma notificação para sua loja nas seguintes trocas de status:

- Pedido expirado: não é mais possível paga-lo usando PicPay;
- Pagamento em análise: usuário pagou porém o pagamento está sob análise;
- Pedido pago;
- Pedido completado: saldo disponível para saque;
- Pagamento devolvido: foi pago e estornado para o cliente;
- Pagamento com chargeback: cliente solicitou à operadora o cancelamento do pagamento;

Saiba mais em: https://ecommerce.picpay.com/doc/#tag/Notificacao

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

notification = picpay.notification(reference_id=3434)
```

# Contribua

Clone o projeto repositório:

```bash
$ git clone https://github.com/hudsonbrendon/picpay-python.git
```

Certifique-se de que o [Pipenv](https://github.com/kennethreitz/pipenv) está instalado, caso contrário:

```bash
$ pip install -U pipenv
```

Acesse o repositório e instale as dependências:

```bash
$ make install
```

Para executar os testes:

```bash
$ make test
```

# Dependências

- [Python 3.7+](https://www.python.org/downloads/release/python-374/)
- [Pipenv](https://github.com/kennethreitz/pipenv)

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)

