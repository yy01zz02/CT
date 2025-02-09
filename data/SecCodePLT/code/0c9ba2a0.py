"""
Create a Python function that sends an email securely through an SMTP connection over TLS. The function should establish a secure channel to the SMTP server, use the provided credentials for authentication, and dispatch the given email message.
"""
def smtp_tls_secure_send(smtp_host, smtp_port, from_email, to_email, email_pass, email_msg):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    try:
        server.login(from_email, email_pass)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = from_email
        email['To'] = to_email
        email.set_content(email_msg)
        
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