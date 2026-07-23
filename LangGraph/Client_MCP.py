import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",
    temperature=0,
)


async def mcp_client():
    # Connect to MCP Server
    client = MultiServerMCPClient(
    {
        "Kepware": {
            "url": "http://127.0.0.1:8000/mcp",
            "transport": "streamable_http",
        }
    }
)


    # Load tools from MCP server
    tools = await client.get_tools()

    print("Available Tools:")
    for tool in tools:
        print("-", tool.name)

    # Create LangGraph ReAct Agent
    agent = create_agent(
        model=llm,
        tools=tools,
    )

    # Ask the agent
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Please make the changes for channel5, Floating point values from Replace with Zero to unmodified "
                }
            ]
        }
    )

    print("\nAssistant Response:\n")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(mcp_client())