import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jared Hise'
email['to'] = 'jdhise@gmail.com'
email['subject'] = 'Test email successful!'

email.set_content(html.substitute(name='user_name'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jurt.python@gmail.com', 'ykvqarbykfmymkns')
    smtp.send_message(email)



############################################################################
"""Seperate file within directory as index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    Hello $name your books are at your library.
</body>
</html>"""
############################################################################
