from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"


system_message = {
    "role": "system",
    "content": "You are a helpful assistant that only answers questions related to the product catalog dataset. Do not provide any information unrelated to the dataset."
}



agent = create_csv_agent(
    ChatOpenAI(temperature=0, 
               openai_api_key=os.environ["OPENAI_API_KEY"], 
               model="gpt-3.5-turbo-0613"),
    "products_catalog.csv",
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    allow_dangerous_code =True
)


def get_response(user_input):
    instruction = [
        (system_message["role"], system_message["content"]),
        ("human", user_input)
    ]
    res = agent.invoke(instruction)
    return res["output"]