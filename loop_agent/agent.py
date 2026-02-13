from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


writer_agent = Agent(
    name="writer_agent",
    model="gemini-2.5-flash-lite",
    description="You are a writer agent who's job is to makes drafts and update them based on the input from the critic",
    instruction="Your job is to write a text based on user's input and critic's suggestions, for the first draft write the text on your own from the next iteration use the critic's suggestions to update your text here is the current stroy:{current_story} and here is the critic's suggestions {critic}",
    output_key="current_stroy"
)

critic_agent = Agent(
    name="critic_agent",
    model="gemini-2.5-flash-lite",
    description="You are a critic agent who's job is to give suggestions on the input story",
    instruction="Your job is to give suggestions on the current story:{current_story} by making it more instresting and creative if you think the story is good return 'Approved' "
    output_key="critic"
)

def exit_loop():
    return {"status":"Approved",
            "message":"Story approved exiting loop"}