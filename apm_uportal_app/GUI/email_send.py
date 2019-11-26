import smtplib
from email.message import EmailMessage

username = 'apmadmin@autopartmine.com'
password = 'apmadmin@0011'

contacts = ['fathimamasood48@gmail.com', 'fahadbaig663@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'This is a test'
msg['From'] = username
msg['To'] = contacts

msg.set_content('Plain Text Message')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(username, password)
	smtp.send_message(msg)