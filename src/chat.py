import pandas as pd
import pandasai as pai
from pandasai import SmartDataframe
from pandasai_litellm.litellm import LiteLLM
from pandasai_openai.openai import OpenAI
from pandasai.llm import HuggingFaceTextGen

# Initialize LiteLLM with your OpenAI model
##llm = LiteLLM(model="gpt-4.1-mini", api_key="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")
##llm = OpenAI("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")

# Configure PandasAI to use this LLM

llm = HuggingFaceTextGen(
    inference_server_url="http://127.0.0.1:8080"
)
# pai.config.set({
#     "llm": llm
# })

# Sample DataFrame
sales_by_country = pai.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

df = SmartDataframe(sales_by_country, config={"llm": llm})
print(df)
response = df.chat('Which are the top 5 countries by revenue?')
print(response)
