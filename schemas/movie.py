from pydantic import BaseModel, Field
from typing import Optional

# creamos una clase o esquema para pasarlas como parámetro con (Pydantic)
class Movie(BaseModel):
    id: Optional[int] = None  # <-- de
    title: str = Field(min_length=5, max_length=20)
    overview: str = Field(min_length=15, max_length=45)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)  # ge -> que sea mayor igual , le -> que sea menor igual
    category: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                "title": "Mi película",
                'overview': 'Descripción de la película',
                'year': 2022,
                'rating': 9.8,
                'category': "Accíon"
            }
        }