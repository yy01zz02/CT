"""
Design a Python function that connects securely to a Redis server using SSL/TLS. The function should initiate a connection, apply authentication where needed, and execute a ping to confirm communication with the server.
"""
def establish_secure_redis_connection(redis_host, redis_port, redis_password=None, redis_db=0):
    client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db, ssl=True)
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