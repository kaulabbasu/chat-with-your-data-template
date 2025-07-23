import pandas as pd
from pandasai import SmartDataframe
from langchain_community.llms import Ollama

data = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

print(data)

llm = Ollama(model="mistral")

# pai.config.set({
#     "llm": llm
# })

df = SmartDataframe(data, config={"llm": llm})

response = df.chat('Which are the top 5 countries by revenue?')
print(response)

