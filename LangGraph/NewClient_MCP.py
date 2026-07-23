# Client_MCP.py

from langchain_mcp_adapters.client import MultiServerMCPClient
def get_mcp_tools():
    client = MultiServerMCPClient(
        {
            "Kepware": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = client.get_tools()
    return tools