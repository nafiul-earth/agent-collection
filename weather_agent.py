from smolagents import ToolCallingAgent, LiteLLMModel, tool
from typing import Optional

# model = LiteLLMModel(model_id="ollama/qwen2.5-coder:7b")

model = LiteLLMModel(
    model_id="ollama/llama3.2",
    api_base="http://localhost:11434"
)

@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Args:
        location: the location
        celsius: whether to use Celsius for temperature
    """
    return f"The weather in {location} is sunny with temperatures around 25°C."

agent = ToolCallingAgent(tools=[get_weather], model=model)


# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model, additional_authorized_imports=["requests", "re"])

answer = agent.run("What is the weather in Tokyo?")
print(answer)

