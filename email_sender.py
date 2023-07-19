import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jared Hise'
email['to'] = 'jdhise@gmail.com'
email['subject'] = 'Test email successful!'

email.set_content(html.substitute(name='Sjplummer'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jurt.python@gmail.com', 'ykvqarbykfmymkns')
    smtp.send_message(email)
