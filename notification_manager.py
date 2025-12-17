from twilio.rest import Client
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.email_user = os.environ.get("EMAIL_USER")
        self.email_pass = os.environ.get("EMAIL_PASS")
        self.to_email = os.environ.get("MY_EMAIL")

    def send_mail(self, subject, message):
        if self.email_user and self.email_pass:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(self.email_user, self.email_pass)
                connection.sendmail(
                    from_addr=  self.email_user,
                    to_addrs= self.to_email,
                    msg = f"Subject: {subject}\n\n {message}"
                    )
                print("Email Sent!")