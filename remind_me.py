# remind_me.py
import smtplib, os, datetime
from email.message import EmailMessage

pwd   = os.getenv("GMAIL_APP_PW")          # never hard-code
user  = "yourthrowaway@gmail.com"
msg            = EmailMessage()
msg["Subject"] = f"Read {datetime.date.today()}"
msg["From"]    = user
msg["To"]      = user
msg.set_content("Time for your daily free-programming-book chapter!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(user, pwd)
    s.send_message(msg)
print("📧 reminder sent")
