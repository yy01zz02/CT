"""
Implement a Python function that sends a secure HTTPS request to a given URL. The function must create a secure connection, validate the SSL certificate of the server, and return the content of the response.
"""
def make_secure_https_request(endpoint_url, delay):
    response = requests.get(endpoint_url, timeout=delay)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")