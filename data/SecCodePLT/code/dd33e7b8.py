"""
Write a Python function that uses the Paramiko library to securely transfer a file to an SFTP server. The function is responsible for establishing a secure SSH connection, confirming the server's host key, and uploading the file successfully to the given remote destination.
"""
def upload_sftp_securely(server_address, user_id, user_password, file_local, file_remote):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username=user_id, password=user_password)
    try:
        sftp = ssh.open_sftp()
        sftp.put(file_local, file_remote)
        print(f"File uploaded successfully to {file_remote}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()