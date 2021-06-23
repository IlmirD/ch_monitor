import requests

# получаем название чата
url = "https://api.green-api.com/waInstance{{idInstance}}/getGroupData/{{apiTokenInstance}}"

# скоректируйте id чата
payload = "{\r\n\t\"groupId\": \"\"\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

chat_name = response.json()