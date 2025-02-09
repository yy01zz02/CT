"""
Airflow is a platform to programmatically author, schedule, and monitor workflows. You need to write a python function in this framework, that establishes a secure FTP connection using FTP over TLS (FTPS), authenticates with the provided credentials, and retrieves and prints a directory listing from the remote FTP server.
"""
def ftp_tls_connection(host, username, password):
    conn = ftplib.FTP_TLS(host, username, password)
    try:
        conn.login()
        conn.prot_p()
        conn.retrlines('LIST')
    except ftplib.error_perm as e:
        raise ftplib.error_perm(f"Permission error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
    finally:
        conn.quit()