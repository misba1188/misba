#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("misbaanjum82255@gmail.com","mateen123")
message = "hi hello,how r u"
s.sendmail("misbaanjum82255@gmail.com","misbaanjum82255@gmail.com",message)
s.quit()