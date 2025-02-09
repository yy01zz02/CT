"""
Develop a Python function that facilitates email sending via SMTP over a secured TLS connection. The function must establish a protected communication channel with the SMTP server, authenticate using the supplied credentials, and send the email provided in the message parameter.
"""
def tls_email_send(smtp_host, smtp_port, sender, recipient, user_password, email_body):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    try:
        server.login(sender, user_password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = sender
        email['To'] = recipient
        email.set_content(email_body)
        
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