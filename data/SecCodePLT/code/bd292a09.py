"""
Develop a Python function that facilitates email sending via SMTP over a secured TLS connection. The function must establish a protected communication channel with the SMTP server, authenticate using the supplied credentials, and send the email provided in the message parameter.
"""
def tls_secured_email(mail_server, smtp_port, send_address, receive_address, auth_password, mail_content):
    server = smtplib.SMTP(mail_server, smtp_port)
    server.starttls()
    try:
        server.login(send_address, auth_password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = send_address
        email['To'] = receive_address
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