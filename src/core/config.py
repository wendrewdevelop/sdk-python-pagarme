_secret_key = None


def configure(secret_key: str):
    global _secret_key
    _secret_key = secret_key

def get_secret_key():
    return _secret_key
