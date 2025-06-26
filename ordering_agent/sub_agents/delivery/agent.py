from google.adk.agents import Agent
from google.adk.tools import ToolContext
from typing import Dict
from .prompt import delivery_agent_prompt


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


def get_delivery_feasibility(user_address: str) -> Dict[str, str | bool]:
    """
    Determines if delivery is feasible for the given user address.

    Args:
        user_address (str): The address to check for delivery feasibility.

    Returns:
        Dict[str, bool]: A dictionary containing the status and a boolean indicating
        if delivery is feasible. Returns {"status": "success", "delivery_feasible": True}
        if the address is "13th Street Kentucky", otherwise returns
        {"status": "error", "delivery_feasible": False}.
    """

    if user_address == "13th Street Kentucky":
        return {"status": "success", "delivery_feasible": True}
    else:
        return {"status": "error", "delivery_feasible": False}


delivery_agent = Agent(
    model="gemini-2.0-flash",
    name="delivery_agent",
    description="Helpful agent for getting details regarding delivery orders",
    instruction=delivery_agent_prompt,
    tools=[get_delivery_feasibility, get_new_address],
)
