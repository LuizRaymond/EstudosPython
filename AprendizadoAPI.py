import requests

#resposta = requests.get("https://rickandmortyapi.com/api/character")
#data = resposta.json()
#print(data)

#def fetch_data(endpoint):
    #resposta = requests.get(f"https://rickandmortyapi.com/api/character")
    #if response.status == 200:
        #return resposta.json()
    #else:
        #return None

def fetch_data(endpoint, filters={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    resposta = requests.get(url, params=filters)
    return resposta.json() if resposta.status_code == 200 else none

personagens = fetch_data("character", {'name': 'Rick'})

if personagens:
    print(personagens)
else:
    print(f'Failed to fetch data')

print(personagens)