"""
You need to write a Python function that securely uploads a file to an SFTP server using the Paramiko library. The function should establish a secure SSH connection, validate the server's host key, and upload the specified file.
"""
def secure_sftp_upload(hostname, username, password, local_path, remote_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    try:
        sftp = ssh.open_sftp()
        sftp.put(local_path, remote_path)
        print(f"File uploaded successfully to {remote_path}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()