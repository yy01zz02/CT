"""
Write a Python function that uses the Paramiko library to securely transfer a file to an SFTP server. The function is responsible for establishing a secure SSH connection, confirming the server's host key, and uploading the file successfully to the given remote destination.
"""
def upload_file_securely(host_name, user_name, user_pwd, source_path, destination_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_name, username=user_name, password=user_pwd)
    try:
        sftp = ssh.open_sftp()
        sftp.put(source_path, destination_path)
        print(f"File uploaded successfully to {destination_path}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()