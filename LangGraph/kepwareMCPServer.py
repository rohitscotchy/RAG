import requests
from requests.auth import HTTPBasicAuth
from mcp.server.fastmcp import FastMCP
from FieldMofication import ChannelModification, FIELD_MAP

mcp = FastMCP("Kepware Server")

BASE_URL = "http://127.0.0.1:57412/config/v1/project"
USERNAME = "Administrator"
PASSWORD = "admin#1234567890"


@mcp.tool()
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


@mcp.tool()
def create_channel(
    channel: str,
    driver: str = "Modbus TCP/IP Ethernet",
):
    """
    Create a Kepware channel.

    Parameters
    ----------
    channel : str
        Required. Name of the channel.

    driver : str, optional
        Optional.
        Defaults to "Modbus TCP/IP Ethernet".
        The caller does not need to provide this parameter unless a different driver is desired.
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
    

@mcp.tool()
def modify_channel(
    channel: str,
    new_name: str | None = None,
    description: str | None = None,
    driver: str | None = None,
    diagnostics: bool | None = None,
    network_adapter: str | None = None,
    ethernet_port: int | None = None,
    ethernet_protocol: int | None = None,
    write_optimization_method: int | None = None,
    write_optimization_duty_cycle: int | None = None,
    floating_point_handling: int | None = None,
    virtual_network: int | None = None,
    transactions_per_cycle: int | None = None,
    network_mode: int | None = None,
    sockets_per_device: int | None = None,
    maximum_sockets_per_device: int | None = None,
):
    """
    Modify one or more properties of an existing Kepware channel.

    Supported updates include:
    --------------------------
    - Rename the channel
    - Change the description
    - Change the driver
    - Enable or disable diagnostics
    - Change the Ethernet port
    - Change the Ethernet protocol
    - Change the write optimization method
    - Change the write optimization duty cycle
    - Change floating point handling
    - Change the virtual network
    - Change transactions per cycle
    - Change network mode
    - Change sockets per device
    - Change maximum sockets per device

    Examples:
    ---------
    Rename Channel10 to Channel20.

    Change Channel10 Ethernet port to 9098.

    Enable diagnostics.

    Rename Channel10 to Channel20 and change the port to 9098.

    Change write optimization method.

    Any combination of supported fields can be updated in a single call.
    """

    try:

        # Read existing configuration
        channel_data = get_channel(channel)

        # Build modifications from supplied arguments
        modifications = {
            "new_name": new_name,
            "description": description,
            "driver": driver,
            "diagnostics": diagnostics,
            "network_adapter": network_adapter,
            "ethernet_port": ethernet_port,
            "ethernet_protocol": ethernet_protocol,
            "write_optimization_method": write_optimization_method,
            "write_optimization_duty_cycle": write_optimization_duty_cycle,
            "floating_point_handling": floating_point_handling,
            "virtual_network": virtual_network,
            "transactions_per_cycle": transactions_per_cycle,
            "network_mode": network_mode,
            "sockets_per_device": sockets_per_device,
            "maximum_sockets_per_device": maximum_sockets_per_device,
        }

        # Remove parameters not supplied
        modifications = {
            k: v for k, v in modifications.items()
            if v is not None
        }

        if not modifications:
            return {
                "message": "No modifications supplied."
            }

        print("\nRequested Modifications:")
        print(modifications)

        # Convert friendly names to Kepware property names
        updates = {}

        for field, value in modifications.items():
            if field not in FIELD_MAP:
                return {
                    "error": f"Unsupported field: {field}"
                }

            updates[FIELD_MAP[field]] = value

        print("\nUpdates:")
        print(updates)

        # Merge into existing payload
        channel_data.update(updates)

        print("\nFinal Payload:")
        import json
        print(json.dumps(channel_data, indent=4))

        url = f"{BASE_URL}/channels/{channel}"

        response = requests.put(
            url,
            json=channel_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10,
        )

        print("\nStatus Code:", response.status_code)
        print("Response Body:", response.text)

        response.raise_for_status()

        # Verify the update
        updated_name = new_name if new_name else channel

        try:
            updated_channel = get_channel(updated_name)
        except Exception:
            updated_channel = None

        return {
            "message": "Channel update request completed.",
            "updated_fields": modifications,
            "verified_configuration": updated_channel
        }

    except requests.exceptions.HTTPError as e:
        return {
            "status": response.status_code,
            "error": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@mcp.tool()
def get_channel_list():
    """
    Retrieve the configuration of all Kepware channels.

    Args:
        channel: Channel name (example: Channel1, Channel2)
    """

    print(f"Tool called with: Channels")

    url = f"{BASE_URL}/channels"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        timeout=10,
    )

    response.raise_for_status()

    return response.json()



@mcp.tool()
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


if __name__ == "__main__":
    print("Starting Kepware MCP Server...")
    mcp.run(transport="streamable-http")