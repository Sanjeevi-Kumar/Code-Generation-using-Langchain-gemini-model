import os
from key import api_key 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st


st.title("Enter the Problem to Slove")
input_=st.text_input("Enter Your Problem")
language=st.text_input("Enter Your Language")
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key,
    temperature=0.7                   
)

prompt_temp=PromptTemplate(
    input_variables=["problem","language"],
    template="Slove this {problem} in {language}"
)
fllm=prompt_temp|llm
if input_:
    answer=fllm.invoke({"problem":input_,"language":language})
    st.write(answer.content)
