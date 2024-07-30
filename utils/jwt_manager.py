from jwt import encode, decode
# Función para crear token

def create_token(data: dict):
    # payload -> el contenido del token, key -> la clave de token, algoritmo -> el algoritmo que usamos para el token
    token: str = encode(payload=data, key="my_secrete_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    # usamos la función decode
    # le pasamos el token generamos con la clave y los algoritmos con los que vamos a descifrar el token
    data: dict = decode(token, key="my_secrete_key", algorithms=['HS256'])
    return data
