import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
import email.encoders as Encoders
import os

USERNAME="smartassistant.drait.edu@gmail.com"
PASSWORD="smartassistant@drait2021"

RECIEVERMAIL="mansoorpasha03111999@gmail.com"
FILENAME="attachem.py"

def sendMail(to,subject,text,files=["college_logo.png"]):
    assert type(to)==list
    assert type(files)==list

    msg=MIMEMultipart()
    msg['From']=USERNAME
    msg['To']=COMMASPACE.join(to)
    msg['Date']=formatdate(localtime=True)
    msg['Subject']=subject
    msg.attach(MIMEText(text))

    for file in files:
        part=MIMEBase('application',"octet-stream")
        part.set_payload(open(file,"rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment;filename="%s"'%os.path.basename(file))
        msg.attach(part)

        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(USERNAME,PASSWORD)
        print("LOGIN SUCCESFULLY")
        server.sendmail(USERNAME,to,msg.as_string())
        print("MAIL SENT TO",RECIEVERMAIL)
        server.quit()

sendMail([RECIEVERMAIL],"Hello Mansoor","This is the body ",[FILENAME])