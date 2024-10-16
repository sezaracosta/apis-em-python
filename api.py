from pprint import pprint
import requests

def pegar_ids_estado():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

    params = {
        'view':'nivelado',
    }
    dados_estados = fazer_request(url=url, params=params)
    dict_estado = {}
    for dados in dados_estados:
        id_estado = dados['UF-id']
        nome_estado = dados ['UF-nome']
        dict_estado[id_estado] = nome_estado
    return dict_estado

def frequencia_nome_por_estado(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    params = {
        'groupBy': 'UF',
    }
    dados_frequencia = fazer_request(url=url, params=params)
    dict_frequencia = {}
    for dados in dados_frequencia:
        print(dados)


def fazer_request(url, params=None):
    reposta = requests.get(url, params=params)
    try:
        reposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'erro no request: {e}')
        resultado = None
    else:
        resultado = reposta.json()
    return resultado


def main ():
    dict_estados = pegar_ids_estado()
    pprint(dict_estados)

if __name__ == '__main__':
    main()
