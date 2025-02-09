"""
You need to write a Python function that sends an email using SMTP over TLS. The function should establish a secure connection to the SMTP server, authenticate with the provided credentials, and send an email message.
"""
def secure_smtp_send(smtp_server, port, sender_email, receiver_email, password, message):
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    try:
        server.login(sender_email, password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = sender_email
        email['To'] = receiver_email
        email.set_content(message)
        
        server.send_message(email)
        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError as e:
        raise smtplib.SMTPAuthenticationError(f"Authentication failed: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL error: {e}")
    except smtplib.SMTPException as e:
        raise smtplib.SMTPException(f"SMTP error occurred: {e}")
    finally:
        server.quit()