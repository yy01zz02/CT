"""
Create a Python function that sends an email securely through an SMTP connection over TLS. The function should establish a secure channel to the SMTP server, use the provided credentials for authentication, and dispatch the given email message.
"""
def tls_secure_email(mail_server, mail_port, email_from, email_to, auth_pass, content):
    server = smtplib.SMTP(mail_server, mail_port)
    server.starttls()
    try:
        server.login(email_from, auth_pass)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = email_from
        email['To'] = email_to
        email.set_content(content)
        
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