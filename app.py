import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM
from pandasai.llm import OpenAI



# setup ollama llm
# ollama = LocalLLM(api_base="http://localhost:11434/v1", model="llama2")

def main():
    st.sidebar.title("Análise de Dados com PandasAI")
    st.sidebar.write("Bem-vindos app de análise de dados com PandasAI")
    st.sidebar.write("")

    llm_key = st.sidebar.text_input("OpenAI key", value="", type="password")

    st.sidebar.write("")
    data_file = st.sidebar.file_uploader("Upload file", type=["csv", "xlsx"])

    st.title("Análise de Dados com PandasAI")
    st.write("Para começar, faça o upload de um arquivo CSV")

    if data_file is not None:
        df = pd.read_csv(data_file)
        st.write(df.head())
        question = st.text_input("Pergunta para os seus dados", value="")

        if st.button("Analyze"):

            if llm_key:
                llm_openai = OpenAI(llm_key)
                sdf = SmartDataframe(df, config={"llm": llm_openai}, name='data_to_analyze')

                st.write("Running LLM")
                response = sdf.chat(question)
                st.write(response)
            else:
                st.write("LLM key is missing")

    pass



if __name__ == "__main__":
    main()
