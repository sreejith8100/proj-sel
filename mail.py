import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "sreejith.sathiakumar@gmail.com"
receiver_email = "sreelakshmi.sathyakumar@gmsil.com"
password = input("Type your password and press enter: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for x in range(0,100):
        message = """\
        Subject: DUMMI


        """ + "DUMMI "*x
        server.sendmail(sender_email, receiver_email, message)
