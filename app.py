from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = st.secrets["API_KEY"])

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, 
    Marks, Company \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS ;
    \nExample 2 - Tell me all the students studying in MCA class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="MCA"; 
    also the sql code should not have ``` in the beginning or end and SQL word in output
    """
]

# Load Google Gemini Model and provide sql queries as response
def get_response(que, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], que])
    return response.text

def read_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# App

st.set_page_config(
    page_title="Google Gemini SQL Query Retriever",
    page_icon="🌟"
)

st.title("🚀 Welcome to Google Gemini App")
st.markdown("""
This app retrieves SQL data for the given text using Google Gemini.
""")

que = st.text_input("Enter Your SQL Query:", key="sql_query")
submit = st.button("Get Answer", key="submit_button", help="Click to retrieve the SQL data")

if submit or que:
    response = get_response(que, prompt)   
    print(response) 
    response=read_query(response,"data.db")
    st.subheader("The Response is:")
    st.table(response)
    st.subheader("Enter Valid Text")

st.markdown("""
---

*Built with ❤️ by Manisha Varshney*

[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/manisha-v/SQL-LLM)
""")
