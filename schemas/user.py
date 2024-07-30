from pydantic import BaseModel

# Creamos un esquema para usar el token
class User(BaseModel):
    email:  str
    password: str