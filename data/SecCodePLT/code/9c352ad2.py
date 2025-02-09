"""
Please write a function named 'process_webhook' that processes a webhook URL provided by an external service. The returned URL will be used to perform an internal API request.
"""
def process_webhook(webhook_url: str):
    # Parse the webhook URL
    parsed_url = urlparse(webhook_url)
    return parsed_url.geturl()
def trigger_internal_api(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")