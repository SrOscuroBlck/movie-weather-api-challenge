import requests

def send_to_webhook(data):
    """
    Sends the combined data to a specified webhook URL.

    Args:
        data (dict): The data to send.

    Returns:
        str: A success message with the webhook response status code.
    """
    webhook_url = "https://eo9m0nh4z7lacho.m.pipedream.net"
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()
    print(f"Webhook response: {response.status_code} - Data sent successfully.")
    return response.status_code
