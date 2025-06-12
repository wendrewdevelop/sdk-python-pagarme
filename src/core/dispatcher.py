from .pipeline import pipeline


def dispatch(path: str, method: str, data: dict = None):
    route = pipeline.get(path)

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

    # Executa a função da rota
    return route["function"](data=data)
