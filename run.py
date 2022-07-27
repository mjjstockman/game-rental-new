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
        print("Do you want to:\n 1) Add stock?\n 2) Return a rental?\n "
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
                add_stock()
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
        if int(chosen_action) not in {1, 2, 3, 4, 5, 6}:
            raise ValueError(
                "Must be a whole number between 1 and 6"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again...\n")
        return False

    return True


def add_stock():
    """Adds new game data to games worksheet if data is verified
    """
    print("Please enter stock information.")
    print("Data should be the name of the game, the age restriction and the number adding to stock, seperated by commas")
    print("Eg: Super Mario Galaxy, 5, 3\n")

    data_str = input("Enter your data here:\n")

    stock_data = data_str.split(",")
    validate_add_stock(stock_data)

    # print(f"You want to add {data_str}")

def validate_add_stock(values):
    try:
        if len(values) != 3:
            raise ValueError(
                f"Missing an entry"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
            

add_stock()
#     validate_add_stock(stock_data)

    # while True:
    #     title = input("\nAdd game title:\n")
    #     min_age = input("\nAdd minimum age:\n")
    #     quantity = input("\nAdd how many:\n")
    #     new_stock_info = [title, min_age, quantity]
    #     # print(new_stock_info)
    #     if validate_add_stock(new_stock_info):
    #          print(f"\nYou entered...\n Title: {title}\n "
    #               f"Minimun Age: {min_age}\n"
    #               f"Quantity: {quantity}\n")
    #     else:
    #         add_stock()
            


        # if validate_add_game(new_stock_info):
        #     print(f"\nYou entered...\n Title: {title}\n "
        #           f"Minimun Age: {min_age}\n"
        #           f"Quantity: {quantity}\n")
        #      print(f"\nYou entered...\n Title: {title}\n "
        #           f"Minimun Age: {min_age}\n"
        #           f"Quantity: {quantity}\n")
        #     confirm = input("Enter Y for yes, N for No\n")
        #     confirm_strip_lcase = confirm.strip().lower()
        #     if confirm_strip_lcase == "n":
        #         validate_add_game(new_game_info)
        #         print("from 435 confirm says no")
        #     elif confirm_strip_lcase == "y":
        #         update_worksheet(new_stock_info, "games")
        #         break

# def validate_add_stock(new_stock_info):
#     """Checks all data has been entered and is valid
#     Returns:
#         bool : True if data validates, False if not
#     """
#     if not all(new_stock_info):
#         print("Missing an element, please try again")
#         return False
#     try:
#         int(new_stock_info[1])
#     except:
#         print("min age not a number, please try again")
#     try:
#         int(new_stock_info[2])
#     except:
#         print("quantity not a number, please try again")
#     return True


# add_stock()

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

