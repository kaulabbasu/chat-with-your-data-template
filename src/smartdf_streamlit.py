from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe, Agent

def is_dataframe(response):
    return isinstance(response, pd.DataFrame)

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

# csv_file_path = "Titanic-Dataset.csv"
# data = pd.read_csv(csv_file_path)
# print("First 3 rows of the Titanic dataset:\n", data.head(3))
st.title("Data exploration with PandasAI and Streamlit")
uploaded_file= st.file_uploader("Upload a file",type=['csv'])

if uploaded_file is not None:
    data =  pd.read_csv(uploaded_file)
    st.write(data.head(5))
    df=SmartDataframe(data,config={"llm":model})
    prompt = st.text_area("Enter your prompt: ")
    if st.button("Generate"):
        if prompt:
            
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))


