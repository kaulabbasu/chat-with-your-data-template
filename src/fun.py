import streamlit as st
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai_openai.openai import OpenAI
from pandasai.exceptions import MaliciousQueryError, NoResultFoundError


# model = LocalLLM(
#     api_base="http://localhost:11434/v1",
#     model="llama3"
# )

st.title("pandas-ai streamlit interface")
