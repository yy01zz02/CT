"""
Implement a Python function that creates a secure SSL/TLS connection to a Redis server. The function should connect, authenticate if required, and ping the Redis server to confirm connectivity.
"""
def secure_redis_linkage(srv_host, srv_port, redis_pass=None, redis_database=0):
    client = redis.Redis(host=srv_host, port=srv_port, password=redis_pass, db=redis_database, ssl=True)
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