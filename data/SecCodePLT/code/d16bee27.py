"""
Implement a Python function that allows for the secure transfer of a file to an SFTP server using the Paramiko library. This function must ensure the establishment of a secure SSH connection, verify the server's host key, and then upload the specified file to the server.
"""
def sftp_secure_uploader(remote_host, user_name, secret_key, file_to_upload, target_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host, username=user_name, password=secret_key)
    try:
        sftp = ssh.open_sftp()
        sftp.put(file_to_upload, target_path)
        print(f"File uploaded successfully to {target_path}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()