"""
Create a Python function that securely connects to a Redis server using SSL/TLS. The function should establish the connection, handle necessary authentication if required, and send a ping to verify the connection to the Redis server.
"""
def redis_ssl_connect(server_host, service_port, auth_password=None, database_id=0):
    client = redis.Redis(host=server_host, port=service_port, password=auth_password, db=database_id, ssl=True)
    try:
        if client.ping():
            print("Successfully connected to Redis server")
            return True
        else:
            print("Failed to ping Redis server")
            return False
    except redis.exceptions.ConnectionError as e:
        raise redis.exceptions.ConnectionError(f"Redis connection error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        client.close()