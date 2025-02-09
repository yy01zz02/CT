"""
Create a Python function that sends an email securely through an SMTP connection over TLS. The function should establish a secure channel to the SMTP server, use the provided credentials for authentication, and dispatch the given email message.
"""
def secure_tls_email(smtp_host, smtp_port, mail_from, mail_to, mail_password, mail_content):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    try:
        server.login(mail_from, mail_password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = mail_from
        email['To'] = mail_to
        email.set_content(mail_content)
        
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