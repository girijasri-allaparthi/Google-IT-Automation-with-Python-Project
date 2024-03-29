#!/usr/bin/env python3
######email the generated pdf to the supplier
import email.message
import mimetypes
import os.path
import smtplib

def generate_report(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
  # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

  # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

    return message
######email.py########
def send(message):
    """Sends the message to the configured SMTP server."""
    localhost = socket.gethostbyname(localipaddress)
    mail_server = smtplib.SMTP(localhost)
    mail_server.send_message(message)
    mail_server.quit()
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER')"
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

generate_report(sender, receiver, subject, body, ".//OneDrive//Desktop//report.pdf")
send(message)
