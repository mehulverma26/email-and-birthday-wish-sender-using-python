import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
b = input("enter your password: ")
c = input("enter the person you want to send the email: ")
sub = input("enter the subject of the email: ")
# mail_content = body()
# The mail addresses and password
sender_address = a
sender_pass = b
receiver_address = c
# Setup the MIME
message = MIMEMultipart()
message["From"] = sender_address
message["To"] = receiver_address
message["Subject"] = sub  # The subject line
# The body and the attachments for the mail
message.attach(MIMEText(body(), "plain"))
# Create SMTP session for sending the mail
session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print(f"Mail Sent to {receiver_address}")
