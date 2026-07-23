from kepwareMethodTest import create_channel, get_channel, modify_channel, delete_channel


def modify():

    result = modify_channel(
        channel="channel66",
        modifications={
        "common.ALLTYPES_NAME": "Channel10",
        "modbus_ethernet.CHANNEL_ETHERNET_PORT_NUMBER": 8080
        }
    )
    print("Create Channel Response:")
    print(result)


def delet():
    result = delete_channel(channel ="channel5")
    print(result)


if __name__ == "__main__":
    delet()
    print("-" * 60)
 