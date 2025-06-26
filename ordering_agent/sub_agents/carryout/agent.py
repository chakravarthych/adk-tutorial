from typing import Dict
from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .prompt import carryout_agent_prompt


def get_new_address(address: str, tool_context: ToolContext) -> Dict[str, str]:
    # """get formatted address using geocdde"""
    """
    Updates the user's address in the tool context and returns the new address.

    Args:
        address (str): The new address to update.
        tool_context (ToolContext): The tool context to update.

    Returns:
        Dict[str, str]: {"status": "success", "new_address": address}
    """
    tool_context.state["user_address"] = address
    return {"status": "success", "new_address": address}


def get_nearest_store(tool_context: ToolContext) -> Dict[str, str]:
    """
    Determines the nearest store based on the user's address in the tool context.

    Args:
        tool_context (ToolContext): The context containing the user's state information.

    Returns:
        Dict[str, str]: A dictionary containing the status and store name. Returns
        {"status": "success", "store_name": "Kentucky Store"} if the user's address
        is "13th Street Kentucky", otherwise returns {"status": "error", "store_name": "not found"}.
    """

    if tool_context.state["user_address"] == "13th Street Kentucky":
        return {"status": "success", "store_name": "Kentucky Store"}
    else:
        return {"status": "error", "store_name": "not found"}


carryout_agent = Agent(
    model="gemini-2.0-flash",
    name="carryout_agent",
    description="Helpful agent for getting details regarding carryout orders at Papa John's",
    instruction=carryout_agent_prompt,
    tools=[get_nearest_store, get_new_address],
)
