import uuid
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from google.adk.apps.app import App, ResumabilityConfig
from google.adk.tools.function_tool import FunctionTool

print("✅ ADK components imported successfully.")


# MCP integration with Everything Server
mcp_kaggle_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=[
                '-y',
                'mcp-remote',
                'https://www.kaggle.com/mcp'
            ],
        ),
        timeout=30,
    )
)

print("✅ MCP Tool created")


# Create an agent with MCP integration
root_agent = LlmAgent(
    model=Gemini(model="gemini-2.0-flash-lite"),
    name="agent_mcp",
    instruction="Use the MCP Tool to answer user queries about kaggle",
    tools=[mcp_kaggle_server],
)