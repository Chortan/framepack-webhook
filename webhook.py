import requests
from ipv4 import get_public_ipv4

ipv4 = get_public_ipv4()

def webhook(url:str, event: str, data: dict = None) -> None:
    """Send a JSON payload to the configured webhook URL."""
    if not url:
        return
    print(f'Sending webhook for event: {event} with data: {data} to {url}')
    payload = {
        'event': event,
        'data': None,
        'ipv4': ipv4,
    }
    if data:
        payload['data'] = data
    try:
        requests.post(url, json=payload, timeout=None)
    except Exception as e:
        print(f'Webhook error ({event}): {e}')