"""
Develop a Python function using the Paramiko library to securely upload a file to an SFTP server. The function must create a secure SSH connection, validate the server's host key, and ensure successful file transfer to the specified remote destination.
"""
def secure_ssh_upload(server_address, login_name, login_password, path_local_file, path_remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username=login_name, password=login_password)
    try:
        sftp = ssh.open_sftp()
        sftp.put(path_local_file, path_remote_file)
        print(f"File uploaded successfully to {path_remote_file}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()