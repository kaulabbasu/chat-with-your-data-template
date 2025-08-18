from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe, Agent

# model
model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

df = SmartDataframe(sales_by_country, config={"llm": model})
print("-----------original dataframe---------------")
print(df)
print("--------------------------------------------")
response = df.chat('Which are the top 5 countries by revenue?')
print("----------dynamic dataframe----------------")
print(response)
print("-------------------------------------------")
