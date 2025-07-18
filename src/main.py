import os
import pandas as pd
from pandasai import Agent
from pandasai import SmartDataframe
from langchain_community.llms import Ollama
from pandasai.llm.local_llm import LocalLLM
    
#llm = Ollama(model="llama3") # e.g., "mistral", "llama3"
    
llm = LocalLLM(api_base="http://localhost:1234/v1") # Adjust API base to your local model server

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
# os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

# agent = Agent(sales_by_country)
# agent.chat('Which are the top 5 countries by sales?')

df = SmartDataframe(sales_by_country, config={"llm": llm})
response = df.chat('Which are the top 5 countries by sales?')
print(response)
