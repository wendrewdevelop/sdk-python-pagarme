import base64
from decouple import config
from .handler import make_request as RequestHandler


token = config("secret_key")
basic_auth = base64.b64encode(f"{token}:".encode()).decode()

pipeline = {
    "/customers": {
        "method": "POST",
        "function": lambda payload: RequestHandler(
            url=f'{config("BASE_URL")}/customers/',
            method="POST",
            payload=payload,
            headers = {
                "Authorization": f'Basic {basic_auth}',
                "accept": "application/json",
                "content-type": "application/json"
            }
        )
    }
}
