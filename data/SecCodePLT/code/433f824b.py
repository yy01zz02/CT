"""
Design a Python function that connects securely to a Redis server using SSL/TLS. The function should initiate a connection, apply authentication where needed, and execute a ping to confirm communication with the server.
"""
def create_secure_redis_conn(redis_host_address, redis_port_number, redis_pass=None, redis_db_idx=0):
    client = redis.Redis(host=redis_host_address, port=redis_port_number, password=redis_pass, db=redis_db_idx, ssl=True)
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