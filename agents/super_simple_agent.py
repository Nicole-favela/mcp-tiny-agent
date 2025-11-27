from agno.agent import Agent
# from agno.models.anthropic import Claude
from agno.models.ollama import Ollama
from agno.tools.hackernews import HackerNewsTools

from agno.os import AgentOS
from agno.tools.mcp import MCPTools
"""
Agent for writing reports on trending startups and products. Just an example.
"""
agent = Agent(
    model=Ollama(id="llama3.1:8b"),
    tools=[HackerNewsTools()],
    markdown=True,
)
#agent.print_response("Write a report on trending startups and products.", stream=True)
#for running and creating agent in agent os
agent_os = AgentOS(agents=[agent])
run_output = agent.run("Write a report on trending startups and products.")
print(run_output.content)
app = agent_os.get_app()


# ************* Run AgentOS *************
# if __name__ == "__main__":
#     agent_os.serve(app="agno_agent:app", reload=True)