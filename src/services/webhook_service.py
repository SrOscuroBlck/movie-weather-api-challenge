import requests

def send_to_webhook(data):
    """
    Sends the combined data to a specified webhook URL.

    Args:
        data (dict): The data to send.

    Returns:
        int: The response status code if successful.
        str: An error message if the request fails.
    """
    webhook_url = "https://eo9m0nh4z7lacho.m.pipedream.net"
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        # Log the error and return an error message
        return f"Error: {str(e)}"
