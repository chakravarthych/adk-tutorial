from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from ...tools.bundle_recommender import set_number_of_people, set_dietary_preferences, add_menu_items
from . import prompt

MODEL = "gemini-2.5-flash"

BundleRecommenderAgent = Agent(
    model=MODEL,
    name="bundle_recommender",
    tools= [set_number_of_people, set_dietary_preferences, add_menu_items],
    instruction=prompt.bundle_recommender_agent_instruction,

)
