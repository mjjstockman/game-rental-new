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


def make_choice():
    """Get choice of action as an input from user
    """
    while True:
        print("Do you want to:\n 1) Make a rental?\n 2) Return a rental?\n "
              "3) Print stock?\n 4) Add a new customer?\n "
              "5) Add a new title?\n 6) Update fines?\n")
        chosen_action = input("Please select from above numbers "
                              "and press Enter:\n")
       
        if validate_chosen_action(chosen_action):
            if int(chosen_action) == 6:
                get_overdue_items()
            elif int(chosen_action) == 5:
                add_game()
            elif int(chosen_action) == 4:
                add_customer()
            elif int(chosen_action) == 3:
                print_stock()
            elif int(chosen_action) == 2:
                input_data(2)
            elif int(chosen_action) == 1:
                input_data(1)
            break


def validate_chosen_action(chosen_action):
    """Checks chosen_action input was an integer between 1 and 6
    Args:
        chosen_action (int) : The input the user entered when choosing
        an action
    Raises:
        ValueError : If chosen_action is not a full number between 1 and 5
    Notes:
        Converts chosen_Action to a string before testing for inclusion
    """
    try:
        if (chosen_action) not in {1, 2, 3, 4, 5, 6}:
            raise ValueError(
                "Must be a whole num between 1 and 6"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True
# def add_stock():
#     """
#     Add opening stock info
#     """
#     print("Please enter stock information.")
#     print("Data should be the name of the game, the age restriction and the number in stock, seperated by commas")
#     print("Eg: Super Mario Galaxy, 5, 3\n")

#     data_str = input("Enter your data here: ")

#     stock_data = data_str.split(",")
#     validate_add_stock(stock_data)


# def validate_add_stock(values):
#     """
#     Inside the try, 

#     Args:
#         values (_type_): _description_
#     """
#     try:
#         if len(values) != 3:
#             raise ValueError(
#                 f"Data have "
#             )


make_choice()

