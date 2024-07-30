from fastapi import APIRouter, Depends, Query, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


# Listamos las películas
# Usamos el response model para decirle como recivirá los datos
# Definimos también la respuesta en la función
# Ponemos el estatus code que debería enviar la función al ejecutarse correctamente
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Filtramos por id (ruta)
# La función Path sirve para dar validaciones a los parametros de las rutas
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movies(id: int = Path(ge=1, le=100)):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Filtramos por categoría (parametros)
# Usamos Query para los parametros de los query
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Agregamos nuevos registros
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movies(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "La película se ha registrado"})


# Modificamos registros
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movies(id: int, movie: Movie):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "se ha modificado una película"})


# Eliminar registro
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movies(id: int):
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "se ha eliminado una película"})
