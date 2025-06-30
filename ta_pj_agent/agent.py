from google.adk.agents import LlmAgent

from . import prompt
from .sub_agents.bundle_recommender import BundleRecommenderAgent
from .sub_agents.store_gen import StoreGenAgent


MODEL = "gemini-2.5-flash"

paige = LlmAgent(
    name="Paige",
    model=MODEL,
    description=(
        "Agent to help with large group or catering orders, guiding users through options and suggesting order quantities based on menu data."
    ),
    instruction=prompt.PAIGE_PROMPT,
    output_key="order_params",
    sub_agents=[
        StoreGenAgent,
        BundleRecommenderAgent,
    ],
)

root_agent = paige
