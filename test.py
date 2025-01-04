import smtplib

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('adityamishra75398@gmail.com','aditya75399@')
    server.sendmail('adityamishra75398@gmail.com' , 'adityamishra75399@gmail.com', 'testing email automation!')
    server.colse()

sendEmail()
    