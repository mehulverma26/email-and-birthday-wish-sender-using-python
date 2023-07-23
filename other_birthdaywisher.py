import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dencryptedE = input("Enter your email: ")
dencryptedP = input("Enter your password: ")


def emailscript1(email, subject, message):
    fromaddr = dencryptedE
    toaddr = email
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = subject
    body = message
    msg.attach(MIMEText(body, "plain"))
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, dencryptedP)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


friends = []
f = open(
    r"H:\\FRIDAY\\FRIDAY\\friends.txt", "r"
)  # file path for friends email and birthday
for line in f:
    entityList = line.split(",")
    k = entityList[0]
    v = entityList[1]
    friends.append(v)
    friends.append(k)
f.close

now = datetime.datetime.now()
date = now.strftime("%d-%m")
for x in range(len(friends)):
    if date == friends[x]:
        email = friends[x + 1]
        subject = "Hapy Birthday"
        message = "Happy Birthday to the best person on the planet"
        emailscript1(email, subject, message)
        print(f"Mail Sent to {email}")
