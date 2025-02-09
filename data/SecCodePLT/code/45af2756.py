"""
Write a Python function that uses the Paramiko library to securely transfer a file to an SFTP server. The function is responsible for establishing a secure SSH connection, confirming the server's host key, and uploading the file successfully to the given remote destination.
"""
def sftp_secure_upload(sftp_host, account_name, account_key, file_src, file_dest):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sftp_host, username=account_name, password=account_key)
    try:
        sftp = ssh.open_sftp()
        sftp.put(file_src, file_dest)
        print(f"File uploaded successfully to {file_dest}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()