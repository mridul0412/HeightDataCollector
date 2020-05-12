from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height,count):
    from_email="pytestsheight@gmail.com"
    from_password="Netid~6313"
    to_email=email

    subject="Height Data"
    message="Hey there! Your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and it is calculated out of <strong>%s</strong> people." % (height,avg_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
