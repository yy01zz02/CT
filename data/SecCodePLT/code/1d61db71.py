"""
You need to write a Python function that makes a secure HTTPS request to a given URL. The function should establish a secure connection, validate the server's SSL certificate, and return the response content.
"""
def secure_https_request(url, timeout):
    response = requests.get(url, timeout=timeout)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")