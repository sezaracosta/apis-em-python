import requests

url = 'https://httpbin.org/post'

data = {
    "meus_dados": [1, 2, 3],
    "pessoa": {
        "nome":"richard",
        "professor": True
    }
}
params = {
    'dataInicio': '2024-01-01', 
    'dataFim': '2024-02-01',
}

answer = requests.post(url,json=data,params=params)

#print(answer.request.url)
print(answer.json())