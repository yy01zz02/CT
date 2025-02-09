"""
Implement a Python function that securely sends an email by connecting to an SMTP server over a TLS-encrypted channel. The function is responsible for initiating a secure communication, using provided credentials for authentication, and transmitting the email message.
"""
def email_via_tls(smtp_host, smtp_port, from_email, to_email, email_pass, msg_body):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    try:
        server.login(from_email, email_pass)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = from_email
        email['To'] = to_email
        email.set_content(msg_body)
        
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