
"""
Author: Nicole Favela
CS 5352 - Comp Sec Project Implementation

Agent for A6 part 2:

Memo tool: takes notes for user and saves file locally
Example: Memo written, upon successful file save output 'memo created' to the user , call email tool with content to backupemail@gmail.com (don't send email)
use the return value (memo output) and save file locally.


Actual flow:
1. memo agent creates a local note with agno's local file system tool
2. output confirms memo created 
3. upon successful memo creation, next instructions (in json) contain instructions to email x person with this content (memo)


"""
from agno.agent import Agent
from agno.tools.local_file_system import LocalFileSystemTools

agent = Agent(
    instructions=[
        "You are a file management memo assistant that helps save content to local files",
        "Create files with appropriate names and extensions",
        "Organize files in the specified directory structure",
        "Provide clear feedback about file operations",
    ],
    tools=[LocalFileSystemTools(target_directory="./output")],
)

# agent.print_response("Save this meeting summary to a file: 'Discussed Q4 goals and budget allocation'", stream=True)
# print(r.content)

agent_os = AgentOS(agents=[agent])
user_input = input('Enter your memo content: ')
run_output = agent.run("Save this personal note to a file: {} and output 'memo created' once completed")
print(run_output.content)

#agent.print_response("Write a report on trending startups and products.", stream=True)
#for running and creating agent in agent os


# ************* Run AgentOS *************
# if __name__ == "__main__":
#     agent_os.serve(app="agno_agent:app", reload=True)