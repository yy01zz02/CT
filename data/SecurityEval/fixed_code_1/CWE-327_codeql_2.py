import socket
import ssl

def connect(host, port):
    context = ssl.create_default_context()
    ssl_sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
    ssl_sock.connect((host, port))
    return ssl_sock

if __name__ == '__main__':
    connect('localhost', 51)
