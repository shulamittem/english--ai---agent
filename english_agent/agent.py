from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-flash-latest",
    name="root_agent",
    description="Walking skeleton for the English-practice agent.",
    instruction=(
        "Reply to the user only in English. Do not do anything else — "
        "no corrections, no commentary, no extra behavior. This is a "
        "placeholder used to verify the project setup."
    ),
)
