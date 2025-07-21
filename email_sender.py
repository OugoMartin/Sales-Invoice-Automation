import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(attachment_path):
    """Send an email with the PDF report attached."""
    msg = EmailMessage()
    msg['Subject'] = 'Daily Sales Report'
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("RECIPIENTS").split(",")
    msg.set_content('Please find the daily sales report attached.')

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=os.path.basename(attachment_path))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)
