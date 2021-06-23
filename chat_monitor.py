import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

from chatHistory import chat_history
from chatName import chat_name

# ключевые слова, по которым идет поиск
key_words = ['алкоголь', 'нет воды', 'нет электричества']

body_of_email = ""

for t in chat_history:
  for kw in key_words:
    if(t['typeMessage'] == 'textMessage' and (kw in t['textMessage'])):
        date = datetime.fromtimestamp(t["timestamp"])
        context = "Номер телефона: {},<br> Сообщение: {},<br> Дата: {},<br> Название чата: {}<br><br><br>".format(t["senderId"][:-5], t["textMessage"], str(date), chat_name['subject'])
        body_of_email += context
        # выводим совпавшие сообщения в консоль
        print('Номер телефона: ' + t["senderId"][:-5])
        print("Сообщение: " +  t["textMessage"])
        print("Дата: " +  str(date))
        print("Название чата: " + chat_name['subject'])
        print('\n')

# send email
sender = '' # email отправителя
receiver = '' # email получателя

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Zuckerberg's spy"
msg['From'] = sender
msg['To'] = receiver

# Create the body of the message (a plain-text and an HTML version).
# отправляем данные на почту в html формате c правильным форматированием
text = ""
html = """\
<html>
  <head></head>
  <body>
    <p>
    Сообщения с ключевыми словами: 
    <br>
    <br>
      {}
    </p>
  </body>
</html>
""".format(body_of_email)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = '', password = '') # нужно отключить защиту в google и сгенерировать пароль для gmail
s.sendmail(sender, receiver, msg.as_string())
s.quit()