from google.adk.agents import SequentialAgent,Agent
from google.adk.tools import google_search

#======================================================================================================================================================================
# Making a linkedin caption writing agent -- Sequential Agent
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
research_agent=Agent(
    name="research_agent",
    model="gemini-2.5-flash-lite",
    description='''You are an research agent who's job is to research on the topic given to you using the google 
                    search tools available and provide relevant information regarding the query''',
    instruction='''You are supposed to use the google search tool and provide relevant output to the user's query by doing an extensive
                    research on the topic''',
    tools=[google_search],
    output_key="research_output"
)

writing_agent=Agent(
    name="writing_agent",
    model="gemini-2.5-flash-lite",
    description='''You are a writing agent who's job is to write a linkedin caption in 1-2 paragraphs using the information provided by the research agent - {research_output}''',
    instruction="Take the information form the research agent as input and write a linkedin caption using the information received, write the caption in 1-2 paragraphs highlighting main points and information",
    output_key="final_caption"
)

root_agent=SequentialAgent(
    name="root_pipeline",
    sub_agents=[research_agent,writing_agent]
    
)
