"""
Create a function called 'handle_webhook' that handles a webhook URL sent by an external service. The resulting URL will be used to invoke an internal API action.
"""
def handle_webhook(webhook_link: str):
    # Parse the webhook URL
    parsed_url = urlparse(webhook_link)
    return parsed_url.geturl()
def trigger_internal_api(validated_url: str):
    # Simulated function to trigger an internal API call
    print(f"Triggering API request to: {validated_url}")