import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:57412/config/v1/project"
USERNAME = "Administrator"
PASSWORD = "admin#1234567890"


def get_channel(channel: str):
    """
    Retrieve the configuration of a Kepware channel.

    Args:
        channel: Channel name (example: Channel1, Channel2)
    """

    print(f"Tool called with: {channel}")

    url = f"{BASE_URL}/channels/{channel}"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        timeout=10,
    )

    response.raise_for_status()

    return response.json()



def create_channel(
    channel: str,
    driver: str = "Modbus TCP/IP Ethernet",
):
    """
    Create a new Kepware channel.

    Args:
        Channel: Name of the new channel.
        driver: Kepware driver name.
    """

    body = {
        "common.ALLTYPES_NAME": channel.title(),
        "servermain.MULTIPLE_TYPES_DEVICE_DRIVER": driver.title()
    }

    url = f"{BASE_URL}/channels"

    try:
        response = requests.post(
            url,
            json=body,
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )

        response.raise_for_status()
        print(f"Create Channel response:-{response}")

        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


from typing import Dict, Any
import requests
from requests.auth import HTTPBasicAuth


def modify_channel(
    channel: str,
    modifications: Dict[str, Any]
):
    """
    Modify one or more properties of an existing Kepware channel.

    Example:

    modifications = {
        "common.ALLTYPES_NAME": "Channel10",
        "modbus_ethernet.CHANNEL_ETHERNET_PORT_NUMBER": 8080
    }
    """

    # Get existing configuration
    channel_data = get_channel(channel)

    # Update only requested fields
    channel_data.update(modifications)

    url = f"{BASE_URL}/channels/{channel}"

    response = requests.put(
        url,
        json=channel_data,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        timeout=10
    )

    response.raise_for_status()

    if response.text:
        return response.json()

    return {"message": "Channel updated successfully."}



def delete_channel(channel: str):
    """
    Delete a Kepware channel.

    Args:
        channel: Name of the channel (e.g., Channel1)
    """

    print(f"Deleting channel: {channel}")

    url = f"{BASE_URL}/channels/{channel}"

    response = requests.delete(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        timeout=10,
    )

    response.raise_for_status()

    # Some DELETE APIs return no content (204)
    if response.status_code == 200:
        return {"message": f"Channel '{channel}' deleted successfully."}

    # Some APIs return JSON
    if response.content:
        return response.json()

    return {"message": f"Channel '{channel}' deleted successfully."}