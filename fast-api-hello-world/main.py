#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI() #declaración del objeto

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None #None es el valor tomado por defecto
    is_married: Optional[bool] = None

@app.get("/") #path operation decorator
def home():
    return {"Hello": "World"}

#request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)): #dentro de la función se declara el request body --> lo que se ve entre parentesis es (parámetro:tipo = Body)
    return person                              #los ... indican que el request es obligatorio

#validation: query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return{name: age}