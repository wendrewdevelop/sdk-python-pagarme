import base64
from decouple import config
from .handler import make_request as RequestHandler
from .config import get_secret_key


pipeline = {
    "/customers": {
        "method": "POST",
        "function": lambda payload: RequestHandler(
            url=f'{config("BASE_URL")}/customers/',
            method="POST",
            payload=payload,
            headers = {
                "Authorization": f'Basic {base64.b64encode(f"{get_secret_key()}:".encode()).decode()}',
                "accept": "application/json",
                "content-type": "application/json"
            }
        )
    }
}
