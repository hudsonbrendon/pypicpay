from decouple import config

from pypicpay import PicPay

picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"),
    x_seller_token=config("X_SELLER_TOKEN"),
)

status = picpay.status(reference_id=102030)

print(status)
