from typing import Optional
from pydantic import BaseModel, Field


class ChannelModification(BaseModel):
    """
    Kepware Channel modification model.

    Only the fields provided by the LLM/user will be updated.
    """

    # ---------------------------
    # General
    # ---------------------------
    new_name: Optional[str] = Field(
        default=None,
        description="New channel name."
    )

    description: Optional[str] = Field(
        default=None,
        description="Channel description."
    )

    driver: Optional[str] = Field(
        default=None,
        description="Device driver name. Example: Modbus TCP/IP Ethernet"
    )

    diagnostics: Optional[bool] = Field(
        default=None,
        description="Enable or disable diagnostics."
    )

    # ---------------------------
    # Ethernet
    # ---------------------------
    network_adapter: Optional[str] = Field(
        default=None,
        description="Ethernet network adapter."
    )

    ethernet_port: Optional[int] = Field(
        default=None,
        description="TCP port number."
    )

    ethernet_protocol: Optional[int] = Field(
        default=None,
        description="Ethernet protocol."
    )

    # ---------------------------
    # Write Optimization
    # ---------------------------
    write_optimization_method: Optional[int] = Field(
        default=None,
        description="Write optimization method."
    )

    write_optimization_duty_cycle: Optional[int] = Field(
        default=None,
        description="Write optimization duty cycle."
    )

    # ---------------------------
    # Floating Point
    # ---------------------------
    floating_point_handling: Optional[int] = Field(
        default=None,
        description="Floating point handling."
    )

    # ---------------------------
    # Communication Serialization
    # ---------------------------
    virtual_network: Optional[int] = Field(
        default=None,
        description="Virtual network."
    )

    transactions_per_cycle: Optional[int] = Field(
        default=None,
        description="Transactions per communication cycle."
    )

    network_mode: Optional[int] = Field(
        default=None,
        description="Communication network mode."
    )

    # ---------------------------
    # Modbus TCP
    # ---------------------------
    sockets_per_device: Optional[int] = Field(
        default=None,
        description="Use one or more sockets per device."
    )

    maximum_sockets_per_device: Optional[int] = Field(
        default=None,
        description="Maximum sockets per device."
    )

FIELD_MAP = {
"new_name": "common.ALLTYPES_NAME",
"description": "common.ALLTYPES_DESCRIPTION",
"driver": "servermain.MULTIPLE_TYPES_DEVICE_DRIVER",
"diagnostics": "servermain.CHANNEL_DIAGNOSTICS_CAPTURE",
"network_adapter": "servermain.CHANNEL_ETHERNET_COMMUNICATIONS_NETWORK_ADAPTER_STRING",
"write_optimization_method": "servermain.CHANNEL_WRITE_OPTIMIZATIONS_METHOD",
"write_optimization_duty_cycle": "servermain.CHANNEL_WRITE_OPTIMIZATIONS_DUTY_CYCLE",
"floating_point_handling": "servermain.CHANNEL_NON_NORMALIZED_FLOATING_POINT_HANDLING",
"virtual_network": "servermain.CHANNEL_COMMUNICATIONS_SERIALIZATION_VIRTUAL_NETWORK",
"transactions_per_cycle": "servermain.CHANNEL_COMMUNICATIONS_SERIALIZATION_TRANSACTIONS_PER_CYCLE",
"network_mode": "servermain.CHANNEL_COMMUNICATIONS_SERIALIZATION_NETWORK_MODE",
"sockets_per_device": "modbus_ethernet.CHANNEL_USE_ONE_OR_MORE_SOCKETS_PER_DEVICE",
"maximum_sockets_per_device": "modbus_ethernet.CHANNEL_MAXIMUM_SOCKETS_PER_DEVICE",
"ethernet_port": "modbus_ethernet.CHANNEL_ETHERNET_PORT_NUMBER",
"ethernet_protocol": "modbus_ethernet.CHANNEL_ETHERNET_PROTOCOL",
}
