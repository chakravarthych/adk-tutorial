from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from ...tools.fetch_store import get_store,geo_code_api,get_last_known_store_address,get_last_known_address,get_order_type
from . import prompt

MODEL = "gemini-2.5-flash"
StoreGenAgent = Agent(
    model=MODEL,
    name="store_gen",
    tools=[get_store,geo_code_api,get_last_known_store_address,get_last_known_address,get_order_type],
    instruction=prompt.store_agent_instruction,
)
