from src import *


payload = {
    "name": "João Silva",
    "email": "joao.silva@example.com",
    "code": "cliente-123",
    "document": "12345678909",  # CPF válido com 11 dígitos
    "document_type": "CPF",
    "type": "individual",
    "gender": "male",
    "birthdate": "01/01/1990",
    "address": {
        "country": "BR",
        "state": "SP",
        "city": "São Paulo",
        "zip_code": "01000000",
        "line_1": "123, Rua da Esperança, Centro",
        "line_2": "Apto 45"
    },
    "phones": {
        "home_phone": {
            "country_code": "55",
            "area_code": "11",
            "number": "23456789"
        },
        "mobile_phone": {
            "country_code": "55",
            "area_code": "11",
            "number": "912345678"
        }
    },
    "metadata": {
        "plano": "premium",
        "referencia": "campanha-maio"
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
