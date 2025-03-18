import smtplib
import os
import mimetypes
from email.message import EmailMessage
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SENDER_EMAIL="bigdataonfleet@gmail.com"
SENDER_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")  # Use an App Password if using Gmail
RECIPIENT_EMAIL = "warticcotaky@gmail.com"
SUBJECT = "Test Email with Attachment"
BODY = "Hello,\n\nPlease find the attached file.\n\nBest regards."
ATTACHMENT_PATH = "sample_data.csv"
msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = SUBJECT
msg.set_content(BODY)
# Attach File
if os.path.exists(ATTACHMENT_PATH):
    mime_type, _ = mimetypes.guess_type(ATTACHMENT_PATH)
    mime_type = mime_type or "application/octet-stream"
    
    with open(ATTACHMENT_PATH, "rb") as attachment:
        msg.add_attachment(attachment.read(),
                           maintype=mime_type.split("/")[0],
                           subtype=mime_type.split("/")[1],
                           filename=os.path.basename(ATTACHMENT_PATH))
else:
    print(f"File not found: {ATTACHMENT_PATH}")


# Send Email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")