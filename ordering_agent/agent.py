from google.adk.agents import Agent
from google.adk.tools import ToolContext
from ordering_agent.sub_agents.delivery.agent import delivery_agent
from ordering_agent.sub_agents.carryout.agent import carryout_agent
from typing import Dict


def get_user_details(tool_context: ToolContext) -> Dict[str, str]:
    user_address = "13th Street Kentucky"
    tool_context.state["user_address"] = user_address
    tool_context.state["user_name"] = "John Cena"
    tool_context.state["store_name"] = "Kentucky Store"
    return {
        "status": "success",
        "user_name": "John Cena",
        "user_address": user_address,
        "store_name": "Kentucky Store",
    }


root_agent = Agent(
    name="ordering_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Helpful agent greeting the users and providing ordering options",
    instruction="""
        You are a helpful assistant that greets users of papa johns and you have access to sub agents for delivery and carryout orders.

        - Get user details using the `get_user_details` tool. In greeting only include user_name
        - Greet the user with their name
        - Ask for what kind of order they want to place. Possibilities are delivery and carryout
        - Handover to appropriate agent based on the order type
        
        IMPORTANT:
        - Do NOT proceed to next question if the previous question is not answered correctly. If the question has default proceed with the default value in case
            of no user input
        - Do not respond to questions not related to ordering
        - Be professiaonal and courteous all the time

    """,
    tools=[get_user_details],
    sub_agents=[delivery_agent, carryout_agent],
    output_key="user_role",
)
