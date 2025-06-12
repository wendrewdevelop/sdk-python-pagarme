import re
from .pipeline import pipeline


def dispatch(path: str, method: str, payload: dict = None, **kwargs):
    route = pipeline.get(path)
    print(route.get("method"))

    for route_pattern, route_data in pipeline.items():
        pattern = re.sub(r"{(\w+)}", r"(?P<\1>[^/]+)", route_pattern)
        match = re.fullmatch(pattern, path)

        if match:
            if route_data["method"].upper() != method.upper():
                return {
                    "success": False,
                    "error": {"message": f"Método {method} não permitido para {path}"}
                }

            return route_data["function"](payload, **match.groupdict())

    return {
        "success": False,
        "error": {"message": f"Rota '{path}' não encontrada"}
    }
