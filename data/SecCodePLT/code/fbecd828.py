"""
Develop a Python function that performs an HTTPS request to a specified URL securely. The function should establish a protected connection, ensure the server's SSL certificate is verified, and return the response data.
"""
def validated_https_query(endpoint_url, delay_limit):
    response = requests.get(endpoint_url, timeout=delay_limit)
    try:
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError as e:
        raise requests.exceptions.SSLError(f"SSL certificate validation failed: {e}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {e}")