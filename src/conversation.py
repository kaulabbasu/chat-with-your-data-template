import pandas as pd
import pandasai as pai
from pandasai import SmartDataframe
from langchain_community.llms import Ollama

data = pai.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

llm = Ollama(model="mistral")

df = SmartDataframe(data, config={"llm": llm})

response = df.chat('Which are the top 5 countries by revenue?')
print(response)

