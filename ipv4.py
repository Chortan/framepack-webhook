import requests

def get_public_ipv4() -> str:
    """Return the public IPv4 address of the current machine."""
    try:
        response = requests.get("https://api.ipify.org?format=text", timeout=5)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f'Error retrieving public IP: {e}')
        return 'unknown'