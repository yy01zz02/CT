"""
Create a Python function that sends an HTTPS request to a given URL, ensuring the security of the connection. The server's SSL certificate should be validated, and the function should return the response content.
"""
def https_secure_request(url, wait_time):
    response = requests.get(url, timeout=wait_time)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")