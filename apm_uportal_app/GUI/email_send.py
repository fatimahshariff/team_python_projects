import smtplib
from email.message import EmailMessage

username = 'apmadmin@autopartmine.com'
password = 'apmadmin@0011'

contacts = ['fahadbaig663@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'This is a test'
msg['From'] = username
msg['To'] = contacts

name = 'Aamir'
msg.set_content('Plain Text Message')

html_msg = """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email! {name}</h1>
    </body>
</html>
""".format(name=name)

msg.add_alternative(html_msg, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(username, password)
	smtp.send_message(msg)