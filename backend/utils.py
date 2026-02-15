import datetime
import smtplib
from twilio.rest import Client

class Utility:
    @staticmethod
    def get_current_datetime():
        """Returns the current UTC date and time in YYYY-MM-DD HH:MM:SS format."""
        return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def send_email(subject, body, to_email):
        """Sends an email with the provided subject and body to the specified email address."""
        # Note: Configure SMTP settings accordingly.
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        from_email = 'your_email@example.com'
        password = 'your_password'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(from_email, to_email, message)

    @staticmethod
    def send_whatsapp_message(to_number, message):
        """Sends a WhatsApp message to the specified number."""
        # Note: Configure Twilio settings accordingly.
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',  # Twilio Sandbox number
            to=f'whatsapp:{to_number}'
        )