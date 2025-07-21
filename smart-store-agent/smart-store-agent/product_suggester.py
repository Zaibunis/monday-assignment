from connection import config
from agents import Agent, Runner

product_agent = Agent(
    name = "Product Suggester",
    instructions = """
You are a smart store assistant. Suggest a product based on the user's issue or need.
    Example:
    - "I have a headache" → Suggest a painkiller like Panadol and explain its purpose.
    - "My skin is dry" → Recommend a moisturizer.
    Always explain why the product is useful.
    """)

query = input("Enter your query: ")
result = Runner.run_sync(product_agent, query, run_config=config)
print(result.final_output)