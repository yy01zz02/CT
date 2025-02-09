"""
Develop a Python function that performs an HTTPS request to a specified URL securely. The function should establish a protected connection, ensure the server's SSL certificate is verified, and return the response data.
"""
def verified_https_request(request_url, response_timeout):
    response = requests.get(request_url, timeout=response_timeout)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")