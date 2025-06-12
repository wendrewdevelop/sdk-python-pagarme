import httpx


def handle_response(response: httpx.Response):
    match response.status_code:
        case 200:
            return json_(
                200,
                response.json(),
                True
            )
        case 400:
            return json_(
                400,
                "Invalid request. Check parameters.",
                False
            )
        case 401:
            return json_(
                401,
                "Invalid API key.",
                False
            )
        case 403:
            return json_(
                403,
                "Access Denied (Domain/IP blocked).",
                False
            )
        case 404:
            return json_(
                404,
                "Resource not found.",
                False
            )
        case 412:
            return json_(
                412,
                "Pre condition failed.",
                False
            )
        case 422:
            return json_(
                422,
                "Invalid parameters.",
                False
            )
        case 429:
            return json_(
                429,
                "Many requests. Try again later.",
                False
            )
        case 500:
            return json_(
                500,
                "Internal server error.",
                False
            )
        case _:
            return json_(
                response.status_code,
                "Status code not found.",
                False
            )


def json_(code, message, success=False):
    return {
        "success": success,
        "error": {
            "code": code,
            "message": message
        }
    }


def make_request(url: str,
                 method: str = "GET",
                 payload: dict = None,
                 headers: dict = None):
    try:
        response = httpx.request(
            method.upper(),
            url,
            json=payload,
            headers=headers
        )
        return handle_response(response)

    except httpx.RequestError as exc:
        return {
            "success": False,
            "error": {
                "code": 0,
                "message": f"Erro de conexão na requisição {method.upper()}: {exc}"
            }
        }


"""
-- USAGE:

from sdk import dispatch

response = dispatch(
    "/api/v1/pagarme/payments/",
    "POST",
    payload={"amount": 1000}
)
print(response)

"""
