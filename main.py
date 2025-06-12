from src import *


payload = {
    "number": "4111111111111111",
    "holder_name": "Joao da Silva",
    "holder_document": "12345678900",
    "exp_month": 12,
    "exp_year": 2028,
    "cvv": "123",
    "brand": "visa",
    "label": "cartao_principal",
    "billing_address": {
        "line_1": "123, Rua Central, Centro",
        "line_2": "Apto 101",
        "zip_code": "01310000",
        "city": "São Paulo",
        "state": "SP",
        "country": "BR"
    },
    "metadata": {
        "tipo": "corporativo",
        "descricao": "Cartão principal do cliente"
    }
}


customer_id = "cus_701VNnF93TZXVqym"

configure(
    secret_key="sk_test_3539be9c0ece44499e6145cd15f58f82"
)

response = dispatch(
    path="/customers",
    method="GET",
    payload=None,
    customer_id=customer_id
)
print(response)
