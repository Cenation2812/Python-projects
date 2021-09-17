import emails
import random


otp = ""
lst = []
 
for i in range(97,123):
  lst.append(chr(i))
 
for i in range(65,90):
  lst.append(chr(i))


def gen_otp(characters):
  otp = ""
 
  for i in range(4):
    otp = otp + random.choice(characters)
 
  
  return otp

 

html_msg = '''<p>Your OTP is'''+ gen_otp(lst) +'''</p>'''

message = emails.html(html=html_msg,
                          subject="trial mail...",
                          mail_from=('Shourjadeep datta', 'shourjadeepdatta@gmail.com'))



mail_via_python = message.send(to=['shourjadeepdatta@gmail.com','vatsaldoshi11@gmail.com','tushdeshpande791@gmail.com'],
                               smtp={'host': 'smtp.gmail.com', 
                                    'timeout': 5,
                                    'port':587,
                                    'user':'shourjadeepdatta@gmail.com',
                                    'password':'dodo2812',
                                    'tls':True})


print(mail_via_python)