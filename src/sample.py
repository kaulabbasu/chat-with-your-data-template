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
st.title("Data analysis with PandasAI")
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

# config = {
#     "llm": model,
    # "enable_cache": False,  # Ensures fresh results
    # "save_logs": True,      # Helps debug errors
    # "verbose": True,        # Prints detailed logs
    # "enable_code_execution": True  # Critical for running generated code
# }

# df_smart = SmartDataframe(data, config=config)
# # response = df.chat('Who is the youngest?')
# print(type(df_smart))
# print(df_smart)

# df_agent = Agent(data, config=config)
# response = df.chat('Who is the youngest?')
# print(type(df_agent))
# print(df_agent)

# response = data  # Start with the original dataframe
# while True:
#     try:
#         prompt = input("\nEnter your prompt (or press Ctrl + C to exit): ")
#         if prompt:
#             print("Generating response...")

#             if not is_dataframe(response):
#                 df_agent = Agent(data, config={"llm": model})

#             response = df_agent.chat(prompt)
#             print("Response:\n", response)

#             if is_dataframe(response):
#                 df_agent = Agent(response, config={"llm": model})
#     except KeyboardInterrupt:
#         print("\nSession terminated by the user. Goodbye!")
#         break
#     except Exception as e:
#         print("An error occurred:", e)
