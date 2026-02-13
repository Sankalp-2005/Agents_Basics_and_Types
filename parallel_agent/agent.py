from google.adk.agents import SequentialAgent, Agent, ParallelAgent
from google.adk.tools import google_search

#======================================================================================================================================================================
# Making a travel planner having whether_checking agent, tickets_checking agent, tourist_destination_suggesting agent, food_suggesting agent, accommodation_checking agent - Parallel Agent
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
whether_check_agent = Agent(
    name="whether_check_agent",
    model="gemini-2.5-flash-lite",
    description='''Weather checking agent''',
    instruction='''Your job is to check the real time current weather status of a location provided by the user and give the relevant information regarding the climate of that area''',
    tools=[google_search],
    output_key="weather"
)
tickets_checking_agent = Agent(
    name="tickets_checking_agent",
    model="gemini-2.5-flash-lite",
    description="Tickets checking agent",
    instruction='''Your job is to check the availability of flight, train and bus tickets from a given location to a given destination given by the user and respond with the cheapest option available, one for each''',
    tools=[google_search],
    output_key="tickets"
)
tourist_destination_suggestion_agent=Agent(
    name="tourist_destination_suggestion_agent",
    model="gemini-2.5-flash-lite",
    description="An agent to check the tourist destinations of a given locations",
    instruction="Your job is to find the tourist destinations from the user given destination location and respond with 5 major attractions of the area",
    tools=[google_search],
    output_key="destinations"
)
food_suggestion_agent=Agent(
    name="food_suggestion_agent",
    model="gemini-2.5-flash-lite",
    description="An agent to suggest food items",
    instruction='''Your job is to find the famous and regional cuisine of a the destination given by user and respond with 5 must try dishes ''',
    tools=[google_search],
    output_key="food"
)
accommodation_checking_agent=Agent(
    name="accommodation_checking_agent",
    model="gemini-2.5-flash-lite",
    description="An agent to check for available accommodations",
    instruction="Your job is to trace the accommodation available around the users entered destination location, covering all types of stay areas like hotels, lodges, paying guest etc and return the top 5 cheapest and high rated accommodation places",
    tools=[google_search],
    output_key="accommodation"
)
aggregator_agent=Agent(
    name="aggregator_agent",
    model="gemini-2.5-flash-lite",
    description="Aggregator Agent",
    instruction="Your job is to aggregate information provided by the accommodation_checking_agent,food_suggestion_agent,tourist_destination_suggestion_agent,tickets_checking_agent and whether_check_agent and provide the user with output information in 5 paragraphs using {accommodation},{food},{destinations},{weather},{tickets}",
    output_key="combined_info"
)

parallel_agent=ParallelAgent(
    name="parallel_agent",
    sub_agents=[accommodation_checking_agent,food_suggestion_agent,tourist_destination_suggestion_agent,tickets_checking_agent, whether_check_agent]
)

root_agent=SequentialAgent(
    name="root_agent",
    sub_agents=[parallel_agent,aggregator_agent]
)

