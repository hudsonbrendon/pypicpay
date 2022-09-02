from decouple import config

from pypicpay import PicPay

picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"),
    x_seller_token=config("X_SELLER_TOKEN"),
)

notification = picpay.notification(reference_id=3434)

print(notification)
