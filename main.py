from fastapi import FastAPI, Query, Path, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routes.movie import movie_router
from routes.user import user_router
from services.movie import MovieService

app = FastAPI()
# Ponemos características a la documentación
app.title = 'API de prueba'  # Título
app.version = '0.0.1'  # versión
# añadimos los middlewares
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)


# Rutas
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hola mundo</h1>')



