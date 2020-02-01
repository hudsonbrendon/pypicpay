# PicPay Python

Aceite PicPay e faça parte do movimento que está revolucionando a relação com o dinheiro no Brasil.

![Python package](https://github.com/hudsonbrendon/picpay-python/workflows/Python%20package/badge.svg?branch=master)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/picpay-python.svg?style=flat)](https://github.com/hudsonbrendon/picpay-python/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![PicPay](logo.png)

# Instalação

```bash
$ pip install picpay-python
```
ou

```bash
$ python setup.py install
```

# Recursos Disponíveis

- [x]  Requisição de Pagamento
- [x]  Cancelamento
- [x]  Status
- [x]  Notificação

# Modo de usar

## Requisição de Pagamento

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

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

cancellation = picpay.cancellation(reference_id=102030)
```

## Status

```python
from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

status = picpay.status(reference_id=102030)
```

## Notificação

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

