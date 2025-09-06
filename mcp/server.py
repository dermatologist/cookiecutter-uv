import logging

import click
from mcp.server.fastmcp.server import FastMCP

from .config import configure_mcp_server

logger: logging.Logger = logging.getLogger(__name__)


def register_mcp_tools(mcp: FastMCP) -> None:
    """
    Register tool functions for the FastMCP server instance.
    """
    logger.debug("Registering MCP tools.")

    # * TODO Register routes if required (To handle OAuth etc)
    # from .routes import register_mcp_routes
    # register_mcp_routes(mcp=mcp, server_provider=server_provider)

    #  TODO Register tools here
    # from .tools.search import register_search_tool
    # register_search_tool(mcp)

    pass


@click.command()
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse", "streamable-http"]),
    default="streamable-http",
    show_default=True,
    help="Transport protocol to use",
)
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR"], case_sensitive=False),
    default="INFO",
    show_default=True,
    help="Log level to use",
)
@click.option(
    "--disable-auth",
    is_flag=True,
    default=True,
    show_default=True,
    help="Disable authorization between MCP client and MCP server. [default: False]",
)
@click.pass_context
def main(click_ctx: click.Context, transport, log_level, disable_auth) -> int:
    """
    RA MCP Server - helping you expose any RA Server or API as a MCP Server.
    """
    # Store CLI options in context for downstream access
    click_ctx.ensure_object(dict)
    click_ctx.obj["disable_auth"] = disable_auth

    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="[%(asctime)s] %(levelname)s {%(name)s.%(funcName)s:%(lineno)d} - %(message)s",
    )
    try:
        mcp: FastMCP = configure_mcp_server(disable_auth)
        register_mcp_tools(mcp=mcp)
        logger.info(f"Starting RA MCP server with {transport} transport")
        mcp.run(transport=transport)
    except Exception as ex:
        logger.error(
            f"Unable to run the RA MCP server. Caused by, %s", ex, exc_info=True
        )
        return 1
    return 0
