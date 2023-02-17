from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random
import pandas as pd

df = pd.read_csv('day32/birthday/birthdays.csv')


# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'example@gmail.com'
smtp_password = "jnodlivyucejxddj"

# Set up the message details
sender_email = 'example@gmail.com'
recipient_email = df['email'].values[0]
subject = 'Happy Birthday'

now = dt.datetime.now()
day = now.day
month = now.month
body = ''
if (day == df['day']).any() and (month == df['month']).any():
    birthday_person = df['name'].values[0]
    print(birthday_person)
    file_path = f"day32/birthday/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person)
        body = contents

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
