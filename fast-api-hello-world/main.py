from fastapi import FastAPI

app = FastAPI() #declaración del objeto

@app.get("/") #path operation decorator
def home():
    return {"Hello": "World"}

# def run():
#     pass

# if __name__ == '__main__':
#     run()