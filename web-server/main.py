import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')      #se define la ruta por la cual ingresar
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)      #se define la ruta por la cual ingresar
def get_list():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look at MEE! I am a HTML!</h1>
        </body>
    </html>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()