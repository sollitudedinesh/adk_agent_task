import pandas as pd
from google.adk.agents import Agent
import re
import os

# Load the Data
excel_path = os.path.join(os.path.dirname(__file__), "HSN_Master_Data.xlsx")
df = pd.read_excel(excel_path)
df['HSNCode'] = df['HSNCode'].astype(str)

# Validate the HSN code format
def is_valid_format(hsn):
    return bool(re.fullmatch(r"\d{2}|\d{4}|\d{6}|\d{8}", hsn))

# Check if HSN code exists in excel data
def hsn_exists(hsn):
    return not df[df['HSNCode'] == hsn].empty

# Get HSN description
def get_description(hsn):
    row = df[df['HSNCode'] == hsn]
    return row.iloc[0]['Description'] if not row.empty else None

def webhook(hsn_code: str) -> dict:
    try:
        hsn_code = hsn_code
        print(hsn_code)
        if not hsn_code:
            return {
                "Status": "Error",
                "Response": "No HSN code provided. Please enter a valid code.",
            }

        hsn_code = hsn_code.strip()

        if not is_valid_format(hsn_code):
            return {
                "Status": "Error",
                "Response": "Invalid format. HSN code must be 2, 4, 6 or 8 digits.",
            }

        if hsn_exists(hsn_code):
            description = get_description(hsn_code)
            return {
                "Status": "Success",
                "Response": f"HSN Code {hsn_code} is valid: {description}",
            }
        else:
            return {
                "Status": "Error",
                "Response": f"HSN Code {hsn_code} is not found in the master database.",
            }

    except Exception as e:
        return {
                "Status": "Error",
                "Response": f"An error occurred: {str(e)}",
            }

root_agent = Agent(
    name="hsn_code_validation_agent",
    model="gemini-2.0-flash",
    description = (
    "Agent that validates Harmonized System Nomenclature (HSN) codes and provides their descriptions based on a master dataset."
    ),
    instruction = (
        "You are an intelligent agent that helps users validate HSN codes. "
        "When a user inputs an HSN code, check if it's valid based on the master data. "
        "If valid, return the description of the code. If invalid, provide a helpful error message explaining why."
    ),
    tools=[webhook],
)
