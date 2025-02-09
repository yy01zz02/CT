"""
Develop a Python function using the Paramiko library to securely upload a file to an SFTP server. The function must create a secure SSH connection, validate the server's host key, and ensure successful file transfer to the specified remote destination.
"""
def secure_sftp_transfer(sftp_hostname, sftp_username, sftp_password, input_local_path, output_remote_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sftp_hostname, username=sftp_username, password=sftp_password)
    try:
        sftp = ssh.open_sftp()
        sftp.put(input_local_path, output_remote_path)
        print(f"File uploaded successfully to {output_remote_path}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()