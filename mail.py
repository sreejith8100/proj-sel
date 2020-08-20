import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "me@gail.com" #sender's email id
receiver_email = "you@gmail.com" #recipient's email id
password = input("Type your password and press enter: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
