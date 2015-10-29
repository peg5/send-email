#! /ur/bin/python3

import smtplib
import getpass

pw = getpass.getpass()
print('Type your email address. ')
email = input()
print('Type the address of the recipient. ')
recipient = input()
print('Type the subject. ')
subject = input()
print('Type your message. ')
message = input()

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
smtpObj.login(email, pw)
smtpObj.sendmail(email, recipient, 'Subject: %s\n%s' % (subject, message))
smtpObj.quit()

print('Message sent.')
