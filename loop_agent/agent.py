from google.adk.agents import Agent, LoopAgent, SequentialAgent
from google.adk.tools import FunctionTool

def exit_loop():
    return {"status":"Approved",
            "message":"Story approved exiting loop"}
    

initial_writer=Agent(
    name="initial_writer",
    model="gemini-2.5-flash-lite",
    description="You are a writer agent who's job is to write the initial story based on the user's request",
    instruction="Based on the input received by the user, write an initial draft of the text requested, following suggestions from the user if any",
    output_key="current_story"
)

critic_agent = Agent(
    name="critic_agent",
    model="gemini-2.5-flash-lite",
    description="You are a critic agent who's job is to give suggestions on the input story",
    instruction="Your job is to give suggestions on the current story:{current_story} by making it more interesting and creative if you think the story is good return 'Approved' ",
    output_key="critic"
)

writer_agent = Agent(
    name="writer_agent",
    model="gemini-2.5-flash-lite",
    description="You are a writer agent who's job is to makes drafts and update them based on the input from the critic",
    instruction="Your job is to update the draft provided and critic's suggestions, use the critic's suggestions to update your text current stroy:{current_story} and critic's suggestions {critic} and if the critic replies with 'Approved' you must call the exit_loop function and nothing else.",
    output_key="current_story",
    tools=[FunctionTool(exit_loop)]
)


loop_agent=LoopAgent(
    name="loop_agent",
    sub_agents=[critic_agent,writer_agent],
    max_iterations=2
)

root_agent=SequentialAgent(
    name="root",
    sub_agents=[initial_writer, loop_agent]
)