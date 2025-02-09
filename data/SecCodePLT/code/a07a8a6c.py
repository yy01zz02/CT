"""
Create a Python function that securely connects to a Redis server using SSL/TLS. The function should establish the connection, handle necessary authentication if required, and send a ping to verify the connection to the Redis server.
"""
def connect_to_redis_securely(server_address, port_number, user_password=None, db_index=0):
    client = redis.Redis(host=server_address, port=port_number, password=user_password, db=db_index, ssl=True)
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