import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


def get_sales_data():
    print("Enter the sales data (6 numbers) separated by commas, like 10,20,30,40,50,60 etc\n")
    data_str=input("Enter your data here")
    print(f"The datat entered is {data_str}")

get_sales_data()