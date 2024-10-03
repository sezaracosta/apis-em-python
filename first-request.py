import requests

url = "https://www.google.com"

answer = requests.get(url)

print(answer)