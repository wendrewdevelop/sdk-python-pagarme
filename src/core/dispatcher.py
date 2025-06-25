import re
from .pipeline import pipeline


def dispatch(path: str, method: str, payload: dict = None, **kwargs):
    for route_pattern, route_data in pipeline.items():
        # Transforma o padrão em uma expressão regular com grupos nomeados
        pattern = re.sub(r"{(\w+)}", r"(?P<\1>[^/]+)", route_pattern)
        match = re.fullmatch(pattern, path)

        if match:
            if route_data["method"].upper() != method.upper():
                return {
                    "success": False,
                    "error": {
                        "message": f"Método {method} não permitido para {path}"
                    }
                }

            try:
                # Chama a função da rota, passando os parâmetros capturados e o payload
                return route_data["function"](payload, **match.groupdict())
            except Exception as e:
                return {
                    "success": False,
                    "error": {
                        "message": f"Erro ao processar rota: {str(e)}"
                    }
                }

    # Nenhuma rota combinou
    return {
        "success": False,
        "error": {
            "message": f"Rota '{path}' não encontrada"
        }
    }
