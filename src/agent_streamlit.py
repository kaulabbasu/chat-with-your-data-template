from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import Agent

def is_dataframe(response):
    return isinstance(response, pd.DataFrame)

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

config={"llm":model}

st.title("Data exploration with PandasAI and Streamlit")
uploaded_file= st.file_uploader("Upload a file",type=['csv'], key='first')
uploaded_second_file= st.file_uploader("Upload a file",type=['csv'], key='second')

# response = data  # Start with the original dataframe
if uploaded_file is not None and uploaded_second_file is not None:
    # csv_file_path = "src/countries.csv"
    data = pd.read_csv(uploaded_file)
    language_data = pd.read_csv(uploaded_second_file)
    response = data
    response_second = language_data
    st.write(data.head(5))
    st.write(language_data.head(5))
    df_agent = Agent(dfs=[data, language_data],config=config)
    while True:
        try:
            #prompt = input("\nEnter your prompt (or press Ctrl + C to exit): ")
            prompt = st.text_area("Enter your prompt: ")
            if st.button("Generate"):          
                if prompt:
                    with st.spinner("Generating response..."):
                        st.write(df_agent.chat(prompt))
                    # print("Generating response...")

                    if not is_dataframe(response) or not is_dataframe(response_second):
                        df_agent = Agent(dfs=[data, language_data],config=config)

                    response = df_agent.chat(prompt)
                    print("Response:\n", response)

                    if is_dataframe(response) and is_dataframe(response_second):
                        df_agent = Agent(dfs=[data, language_data],config=config)
        except KeyboardInterrupt:
            print("\nSession terminated by the user. Goodbye!")
            break
        except Exception as e:
            print("An error occurred:", e)

