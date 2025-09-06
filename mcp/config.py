import logging
import os
from typing import Dict

from mcp.server.auth.settings import AuthSettings, ClientRegistrationOptions
from mcp.server.fastmcp.server import FastMCP
from pydantic import AnyHttpUrl

logger: logging.Logger = logging.getLogger(__name__)


def configure_mcp_server(disable_auth: bool) -> FastMCP:
    """
    Configure and instantiate the FastMCP server instance.
    Returns a FastMCP instance.
    """
    fastmcp_kwargs: Dict = {
        "name": "RA MCP Server",
        "instructions": "This server implements something",
        "host": os.getenv("MCP_SERVER_HOST", "localhost"),
        "port": int(os.getenv("MCP_SERVER_PORT", 8000)),
        "json_response": True,
        "stateless_http": True,
    }
    return FastMCP(**fastmcp_kwargs)
