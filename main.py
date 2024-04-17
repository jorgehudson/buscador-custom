# Librerías
import requests

# Introducir keyword por consola
keyword = input("Introduce una keyword para buscar: ")

# Configuración del buscador
api_key_search = "aquí_tu_clave_de_custom_search_api"
cx = "aquí_tu_código_cx_del_buscador_"
base_url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": api_key_search,
    "cx": cx,
    "q": keyword,
    "start": 1 # Si quieres que te devuelva resultados a partir de la segunda página de resultados cambia el 1 por un 11
}

response = requests.get(base_url, params=params)
print(response)
data = response.json()
urls = []

if "items" in data:
    for item in data["items"]:
        urls.append(item["link"])

print("Resultados\n\n")
for url in urls:
  print(url)
