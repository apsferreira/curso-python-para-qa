import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resposta.json())