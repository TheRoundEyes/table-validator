from modal.base_api import  GeminiAPI
import pandas as pd


class Validator(GeminiAPI):
    def __init__(self, api_key):
        super().__init__(api_key)

    def validate(self,prompt,model,columns,dataframe):
        model_behaviour = f"""
        You are an expert in the field of Data Engineering and you are tasked to validate tables contents with the given {columns}.
        Your job is to validate and check which rows are not valid based off the other rows in the table.
        You will then give a response on a JSON format with the following fields {columns}
        You will also add an additional column called 
        - Row Number: Which will describe the row number of the error
        - Description of Error: Which will describe the error in the row.
        """
        df_as_text = dataframe.to_string()

        full_prompt = f"{model_behaviour}\n{prompt}\n{df_as_text}"

        response = model.generate_content([full_prompt])

        return response


    def process_file(self,file):
        if file.name.endswith("csv"):
            df = pd.read_csv(file)
            return df