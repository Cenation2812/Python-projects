import smtplib
server = 'smtp.gmail.com'
user = 'royalwebinar@gmail.com'
password = 'royal0708'

recipients = ['shourjadeepdatta@gmail.com', 'sanchita_datta@yahoo.com']
sender = 'royalwebinar@gmail.com'
message = 'Hello World'

session = smtplib.SMTP(server)
# if your SMTP server doesn't need authentications,
# you don't need the following line:
session.login(user, password)
session.sendmail(sender, recipients, message)