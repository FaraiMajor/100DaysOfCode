from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random

# Set up the SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'bowmajor@gmail.com'
smtp_password = "jnodlivyucejxddj"

# Set up the message details
sender_email = 'bowmajor@gmail.com'
recipient_email = 'faraimajor263@gmail.com'
subject = 'Sei Sei Fasto'
