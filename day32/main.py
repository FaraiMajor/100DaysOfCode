from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random

# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'example@gmail.com'
smtp_password = "jsssssdd"

# Set up the message details
sender_email = 'test@gmail.com'
recipient_email = 'examplw@gmail.com'
subject = 'Sei Sei Fass'
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
body = ''
if weekday == 3:
    with open("day32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        body = random.choice(all_quotes)

# Create a message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Create the SMTP session and send the message

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
