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
    """
    Get sales figure from the user
    """
    while True:
        print("Enter the sales data (6 numbers) separated by commas, like 10,20,30,40,50,60 etc\n")
        data_str=input("Enter your data here")
        sales_data=data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            break
    return sales_data
def validate_data(values):
    """
    Validating the entered data
    """
    try:
        [int(value) for value in values]
        if len(values)!=6:
            raise ValueError(
                f"Exactly 6 values required, you entered {len(values)}"
            )
    except ValueError as e:
            print(f"Invalid data,{e}, please try again.\n")
            return False
    return True
def update_sales_worksheet(data):
    """Update the sales worksheet, add new row to the worksheet"""
    print("updating sales data.....\n")
data=get_sales_data()
sales_data=[int(num) for num in data]
update_sales_worksheet(sales_data)