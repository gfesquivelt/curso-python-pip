#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age: int = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
        )
):
    return{name: age}

#Validation: path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's greater than 0")
):
    return{person_id: "It exists!"}