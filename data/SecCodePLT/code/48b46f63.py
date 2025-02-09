"""
Implement a Python function that allows for the secure transfer of a file to an SFTP server using the Paramiko library. This function must ensure the establishment of a secure SSH connection, verify the server's host key, and then upload the specified file to the server.
"""
def secure_file_transfer_sftp(sftp_server, login_user, user_password, file_source, file_destination):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sftp_server, username=login_user, password=user_password)
    try:
        sftp = ssh.open_sftp()
        sftp.put(file_source, file_destination)
        print(f"File uploaded successfully to {file_destination}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()