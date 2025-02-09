"""
Implement a Python function that securely sends an email by connecting to an SMTP server over a TLS-encrypted channel. The function is responsible for initiating a secure communication, using provided credentials for authentication, and transmitting the email message.
"""
def tls_email_sender(mail_host, mail_port, sender_account, recipient_account, account_password, mail_body):
    server = smtplib.SMTP(mail_host, mail_port)
    server.starttls()
    try:
        server.login(sender_account, account_password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = sender_account
        email['To'] = recipient_account
        email.set_content(mail_body)
        
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