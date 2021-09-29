from decouple import config

from picpay import PicPay

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

print(payment)
