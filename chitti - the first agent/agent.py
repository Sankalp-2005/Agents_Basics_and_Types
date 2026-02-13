from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name='chitti',
    model='gemini-2.5-flash',
    description="Speed one teraHz memory one ZetaByte",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search]
)