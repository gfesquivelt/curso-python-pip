import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #retorna el estado de la petición
    print(r.text) #imprime la respuesta como texto
    print(type(r.text)) #retorna el tipo de la respuesta
    categories = r.json() #imprime la respuesta como json
    for category in categories:
        print(category['name'])