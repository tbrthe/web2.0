import mercadopago
import os

def process_payment(user_email):
    sdk = mercadopago.SDK(os.getenv('MERCADO_PAGO_ACCESS_TOKEN'))

    payment_data = {
        "transaction_amount": 100.0,  # El monto que pagas por cada 100 anuncios
        "description": "Pago por visualización de anuncios",
        "payment_method_id": "pix",
        "payer": {
            "email": user_email
        }
    }

    payment_response = sdk.payment().create(payment_data)
    return payment_response
