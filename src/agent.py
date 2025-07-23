import pandas as pd
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM
from pandasai import Agent, SmartDataframe
# from pandasai.llm import CustOpenAI

# Sample DataFrame
sales_by_country = pai.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

# llm = LiteLLM(model="lm_studio/llama-3-8b-instruct", api_base="http://localhost:1234/v1")
# llm = CustOpenAI(api_base= "http://127.0.0.1:1234/v1", model_name = "local-model")
llm = LiteLLM(model="local-model", api_base="http://localhost:1234/v1")

df = SmartDataframe(sales_by_country, config={"llm": llm})
#print(df)
response = df.chat('Which are the top 5 countries by revenue?')
print(response)
