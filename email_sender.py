# email_sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os  # Import the os module

# Directly hardcoded email and password (for testing purposes only)
sender_email = 'workdalvi@gmail.com'
sender_password = 'hzqn hrfc tisd wsab'

def send_email(receiver_email, pdf_path):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Your Cardiovascular Disease Prediction Report'
    body = 'Please find attached your cardiovascular disease prediction report.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    attachment = open(pdf_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    
    # Add the attachment header with the filename
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_path)}')
    msg.attach(part)
    attachment.close()  # Close the file after reading

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Failed to send email. Error: {str(e)}'
