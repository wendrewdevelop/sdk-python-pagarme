from decouple import config
from src import (
    ResponseHandler
)


pipeline = {
    "/customers": {
        "method": "POST",
        "function": lambda: ResponseHandler.make_request(
            url=f'{config("BASE_URL")}/customers/',
            method="POST",
            headers={
                "Authorization": "Basic SEU_TOKEN_BASE64",
                "Content-Type": "application/json"
            }
        )
    }
}
