#Python
from typing import Optional
from enum import Enum #Establecer enumeraciones de strings

#Pydantic
from pydantic import BaseModel
from pydantic import Field #Este modulo permite establecer validaciones dentro de los elementos de la clase(ex. first_name, last_name, age, etc.)

#fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI() #declaración del objeto

#Models

class HairColor(str, Enum):
    white = "white"
    blonde = "blonde"
    brown = "brown"
    black = "black"

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str = Field(...,min_length=1,max_length=50)
    last_name: str = Field(...,min_length=1,max_length=50)
    age: int = Field(...,gt=0,le=115)
    #hair_color: Optional[str] = None #Establecer None es el valor tomado por defecto en campos opcionales
    #hair_color: Optional[HairColor] = Field(default=None) #Se determina que los valores a ingresar sean los de la clase HairColor
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

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

#Validation: request body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(
        ...),
        Location: Location = Body(
        ...
    )
):
    results = person.dict()
    results.update(Location.dict())
    return results