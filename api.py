from pprint import pprint
import requests


url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"


params = {
}

resposta = requests.get(url,params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request: {e}')
    resultado = None
else:
    resultado = resposta.json()
    pprint (resultado)