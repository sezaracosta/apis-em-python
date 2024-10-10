import requests

url = "https://www.google.com"

answer = requests.get(url)

print(answer)
print(answer.text)

with open ('page.google.html', 'w') as file:
    file.write(answer.text)