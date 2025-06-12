from .pipeline import pipeline


def dispatch(path: str, method: str, payload: dict = None, **kwargs):
    route = pipeline.get(path)
    print(route.get("method"))

    if not route:
        return {
            "success": False,
            "error": {"message": f"Rota '{path}' não encontrada"}
        }

    if route["method"].upper() != method.upper():
        return {
            "success": False,
            "error": {"message": f"Método {method} não permitido para {path}"}
        }

    return route["function"](payload, **kwargs)
