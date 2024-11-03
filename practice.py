import requests

api_key = 'c05931cb-a780-4488-a142-bda540bd3b69'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)