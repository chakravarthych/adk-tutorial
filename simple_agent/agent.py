from google.adk.agents import Agent

root_agent = Agent(
    name="simple_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="tool_agent",
    instruction="""
    You are a helpful assistant that answers questions regarding the hospital database.
    - Start by greeting the user
    - Politely ask for their staff_id
    - Use the staff_id to get the user's full name and role
    - If your are not find the staff_id don't answer any further questions from the user. Also dont answer any queries
    before verifying the user role
    """,
)
