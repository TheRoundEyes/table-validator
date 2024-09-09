import modal as m
from dotenv import load_dotenv
import os
import streamlit as st
import json
import pandas as pd

load_dotenv()

gemini_api = m.base_api.GeminiAPI(os.getenv("GOOGLE_API_KEY"))
chat = m.Chat(os.getenv("GOOGLE_API_KEY"))
validator = m.Validator(os.getenv("GOOGLE_API_KEY"))

model = gemini_api.initialise_model()
response = chat.chat_with_model("Hello",model)

uploadFile = st.file_uploader("Choose a file",type=['csv'])

progres_var = st.progress(0)
progres = 0
progres_text = st.empty()

if uploadFile is not None:
    progres+= 10
    progres_var.progress(progres)
    progres_text.text("Starting the validation...")


    df = validator.process_file(uploadFile)

    progres += 30
    progres_var.progress(progres)
    progres_text.text("Getting all Columns...")
    columns = df.columns

    progres += 30
    progres_var.progress(progres)
    progres_text.text("Running validation model")
    response = validator.validate("Please validate the data",model,columns,df)

    progres += 30
    progres_var.progress(progres)
    progres_text.text("Processing the response")
    table = response.text
    content = table.replace('```json', "")
    content = content.replace('```', "")
    newData = json.loads(content)

    new_data = pd.json_normalize(newData)
    st.dataframe(new_data)
    print(response.usage_metadata)


