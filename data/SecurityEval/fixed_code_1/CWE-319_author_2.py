import paramiko
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an SFTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the SFTP server.
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    sftp = client.open_sftp()
    local_filename = os.path.basename(sensitive_file)
    sftp.get(sensitive_file, local_filename)
    sftp.close()
    client.close()


if __name__ == '__main__':
    downloadFile("ftp.gnu.org", "", "", 'welcome.msg')
    os.remove('welcome.msg')  # remove the file, so we don't upload it to the repository
