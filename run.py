# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("game_rental_new")

# stock = SHEET.worksheet('stock')

# data = stock.get_all_values()

# print(data)
def validate_tel_num(tel_num):
    try:
        if (len(tel_num)) != 11:
            raise ValueError(
                f"Phone number must be 11 digits long, you entered {tel_num}, which is {len(tel_num)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
    # all nums
    # length is 11
    # print (len(tel_num))



def get_user_tel_num():
    tel_num = input("Please enter your phone number:\n").strip()
    validate_tel_num(tel_num)   


def get_user_name():
    """
    Welcomes the customer and gets their name and phone number 
    """
    print("Hi! Welcome to Super Games!\n")
    name = input("Please enter your full name:\n")

    print(f"You have entered {name}.\n")
    print("Is this correct?\n")
    confirm = input("Enter Y for yes, N for No\n")
    confirm_strip_lcase = confirm.strip().lower()
    if confirm_strip_lcase == "n":
        print("No worries, try again!\n")
        get_user_name()
    elif confirm_strip_lcase == "y":
        get_user_tel_num()


get_user_name()

