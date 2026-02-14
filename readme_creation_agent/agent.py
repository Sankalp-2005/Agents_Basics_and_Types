from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

def readme_file_write_fn(text:str):
    with open("readme.md","w") as readme:
        readme.write(text)

def readme_file_read_fn(path:str)-> str:
    with open(path,"r") as readme:
        contents = readme.read()
        
    return contents

root_agent = Agent(
    model='gemini-2.5-flash',
    name='read_me_creation_agent',
    description='You are an helpful agent to create a readme.md file for the given code',
    instruction='The user gives you input of a path of file which you are supposed open using the readme_file_read_fn and the contents are passed to you using return from that function you are supposed to understand and analyse thoroughly and write a readme.md file content in form of a string, then you are supposed to call the readme_file_write_fn and pass the text generated to that function as argument and create the readme.md file you are not allowed to do anything else, you only create readme string which need to be professional and insightful to upload in github and use the function tool to create that file., if i face any issue print "issue: specify the issue"',
    tools=[FunctionTool(readme_file_read_fn),FunctionTool(readme_file_write_fn)]
)
