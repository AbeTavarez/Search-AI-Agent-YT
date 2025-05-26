from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools.visit_website import visit_website

load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
search = DuckDuckGoSearchResults()
memory = MemorySaver()

tools = [search, visit_website]

agent = create_react_agent(model, tools, checkpointer=memory)

config = {"configurable": {
    "thread_id": "123abc"
}}

def call_agent(query: str):
    response = agent.invoke({
        "messages": HumanMessage(content=query)
    }, config)


    for message in response["messages"]:
        print(f"=========={message.type}===========")
        print(message.content, '\n')
        
        if hasattr(message, "tool_calls"):
            print(message.tool_calls, '\n')
            
    return response["messages"][-1].content