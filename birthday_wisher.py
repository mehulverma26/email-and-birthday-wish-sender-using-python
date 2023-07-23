"""import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

f=open(r"D:\\FRIDAY\\login.txt","r")
for line in f:
    entityList = line.split(',')
    email=entityList[0]
    password=entityList[1]
dencryptedE = ""
dencryptedP = ""
for letter in email:
    if letter == ' ':
        dencryptedE += ' '
    else:
        dencryptedE += chr(ord(letter) - 5)
for letter in password:
    if letter == ' ':
        dencryptedP += ' '
    else:
        dencryptedP += chr(ord(letter) - 5)
print(dencryptedE)
print(dencryptedP)
def emailscript1(email,subject,message):
    fromaddr = dencryptedE
    toaddr = email
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, dencryptedP) 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()

friends=[]
f=open(r"D:\\FRIDAY\\birthday.txt","r")
for line in f:
    entityList = line.split(',')
    k=entityList[0]
    v=entityList[1]
    friends.append(v)
    friends.append(k)
f.close

now = datetime.datetime.now()
date=now.strftime("%d-%m")
for x in range(len(friends)):
    if date==friends[x]:
        email=friends[x+1]
        subject="Hapy Birthday"
        message="Happy birthday to the best person in the world"
        emailscript1(email,subject,message)"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import datetime


def body():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = "\n".join(lines)
    return text


a = input("enter your email id: ")
b = input("enter the password: ")
sub = "Happy Birthday!!!"
# mail_content = body()
# The mail addresses and password
df = pd.read_excel(
    "D:\\FRIDAY\\birthday.xlsx"
)  # file path for friends email and birthday
today = datetime.datetime.now().strftime("%d-%m")
for index, item in df.iterrows():
    bday = item["Birthday"].strftime("%d-%m")
    if today == bday:
        c = item["Email"]
sender_address = a
sender_pass = b
receiver_address = c
# Setup the MIME
message = MIMEMultipart()
message["From"] = sender_address
message["To"] = receiver_address
message["Subject"] = sub  # The subject line
# The body and the attachments for the mail
message.attach(
    MIMEText(
        """Happy Birthday to the best person on the planet
regards,
Mehul""",
        "plain",
    )
)
# Create SMTP session for sending the mail
session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print(f"Mail Sent to {receiver_address}")
