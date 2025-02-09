"""
Develop a Python function that facilitates email sending via SMTP over a secured TLS connection. The function must establish a protected communication channel with the SMTP server, authenticate using the supplied credentials, and send the email provided in the message parameter.
"""
def smtp_tls_mail_send(mail_host, server_port, user_email, recipient_id, login_password, mail_text):
    server = smtplib.SMTP(mail_host, server_port)
    server.starttls()
    try:
        server.login(user_email, login_password)
        
        email = EmailMessage()
        email['Subject'] = 'Test Email'
        email['From'] = user_email
        email['To'] = recipient_id
        email.set_content(mail_text)
        
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