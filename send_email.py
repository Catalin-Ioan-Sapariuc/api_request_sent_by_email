## Here is the email app password set up for sapariuc@gmail.com: luue pfjc ittr bgnm 
import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465
password = os.getenv("GOOGLE_APP_EMAIL_PWD")

fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'

def send_email(context, sender, receiver, subject, message):

    from_ = sender
    to_ = receiver

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(sender, password)
        #try:
        server.sendmail(sender, receiver, fmt.format(from_, 
                                                     to_, subject, message).encode('utf-8'))
        #except UnicodeEncodeError:
        #    server.sendmail(sender, receiver, message.as_string())
        #server.sendmail(sender_email, receiver_email, message.as_string())

