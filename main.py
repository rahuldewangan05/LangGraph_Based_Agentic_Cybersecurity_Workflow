from langgraph.prebuilt import create_react_agent
from tool import run_nmap
from langchain_anthropic import ChatAnthropic
import os
import getpass

from dotenv import load_dotenv

load_dotenv()


llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

# os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("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")

os.environ["ANTHROPIC_API_KEY"]= os.getenv("ANTHROPIC_API_KEY")
 
tools=[run_nmap]

graph=create_react_agent(llm,tools=tools)
inputs = {"messages": [("user", "scan for google.com")]}
for s in graph.stream(inputs, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()