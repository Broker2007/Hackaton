import requests
import json
# Ваш токен
token = '55c585ec-a98b-4b07-ade4-a3f6afba39a9'
# URL сервера
server_url = 'https://games-test.datsteam.dev/play/snake3d'
# API-метод
api = '/player/move'
url = f"{server_url}{api}"
# Данные для отправки
data = {
    'snakes': []
}
# Заголовки заоса
headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
}
# Выполнение POST-запроса
response = requests.post(url, headers=headers, json=data)
# Сохранение ответа в файл
with open('response.json', 'w') as file:
    file.write(response.text)