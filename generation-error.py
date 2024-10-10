import requests

url = 'https://httpbin.org/post'

answer =  requests.get(url)

try:
    answer.raise_for_status()
except requests.HTTPError as e:
    print(f'Impossivel fazer request!Erro: {e}')
else:
    print('result:')
    print(answer.json)