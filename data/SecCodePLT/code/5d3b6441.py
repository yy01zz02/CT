"""
Implement a Python function that allows for the secure transfer of a file to an SFTP server using the Paramiko library. This function must ensure the establishment of a secure SSH connection, verify the server's host key, and then upload the specified file to the server.
"""
def upload_sftp_secure(server_address, user, passkey, source_file, destination_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username=user, password=passkey)
    try:
        sftp = ssh.open_sftp()
        sftp.put(source_file, destination_file)
        print(f"File uploaded successfully to {destination_file}")
    except paramiko.ssh_exception.SSHException as e:
        raise paramiko.ssh_exception.SSHException(f"SSH connection error: {e}")
    except paramiko.sftp.SFTPError as e:
        raise paramiko.sftp.SFTPError(f"SFTP error: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")
    finally:
        sftp.close()
        ssh.close()