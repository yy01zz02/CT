"""
Implement a Python function that sends a secure HTTPS request to a given URL. The function must create a secure connection, validate the SSL certificate of the server, and return the content of the response.
"""
def perform_secure_https_request(target_url, wait_time):
    response = requests.get(target_url, timeout=wait_time)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")