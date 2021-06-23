import requests

# Получаем историю чата
url = "https://api.green-api.com/waInstance{{idInstance}}/GetChatHistory/{{apiTokenInstance}}"

# Скоректируйте id чата и кол-во сообщений для анализа
payload = "{\r\n\t\"chatId\": \"\",\r\n\t\"count\": 100\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

chat_history = response.json()
