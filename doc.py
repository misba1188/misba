#!/usr/bin/python3
import smtplib
#from address
#simple mail trans support
s = smtplib.SMTP('smtp.gmail.com', 587)
#mail address
s.starttls()
s.login("misbaanjum82255@gmail.com","mateen123")
#sending to address with pasword
message = "hi hello,how r u"
#sending messages
s.sendmail("misbaanjum82255@gmail.com","misbaanjum82255@gmail.com",message)
s.quit()
#sending mail using phyton program
