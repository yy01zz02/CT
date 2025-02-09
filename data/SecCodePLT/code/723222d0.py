"""
You need to write a Python function that establishes a secure connection to a Redis server using SSL/TLS. The function should connect to the server, authenticate if necessary, and perform a simple ping operation to verify the connection.
"""
def secure_redis_connection(host, port, password=None, db=0):
    client = redis.Redis(host=host, port=port, password=password, db=db, ssl=True)
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