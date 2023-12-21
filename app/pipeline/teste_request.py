import requests

api_pokemon = 'https://pokeapi.co/api/v2/pokemon/1'

r = requests.get(api_pokemon)
r.status_code

assert r.status_code == 200