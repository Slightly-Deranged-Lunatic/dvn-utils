import json
from string import capwords
import os

OWD = os.getcwd()
os.chdir("points_to_levels")
with open("outfits_cost.json") as data:
    master_outfits_dict = json.load(data)
os.chdir(OWD)

def main():
    USER_POINTS, HAS_ALL_OUTFITS = get_user_input()
    total_points = find_total_points(USER_POINTS, HAS_ALL_OUTFITS)
    level = 1
    while True:
        level += 1
        total_points -= level * 2
        if total_points <= 0:
            level -= 1
            total_points += level * 2
            break
    print(f"Your level given your points would be {level} with {total_points} points leftover.")
    input("Press enter to close")

def get_user_input():
    # Returns all the user input the program needs.
    # In a function to sort of hide it away from all the code because input validation is gross
    while True:
        try:
            USER_POINTS = int(input("Enter how many points you have: "))
            break
        except ValueError:
            print("Please only put in a whole number.")

    while True:
        VALID_INPUT = ["yes", "no"]
        try:
            HAS_ALL_OUTFITS = input("Do you have every outfit? (yes or no): ").lower()
            if HAS_ALL_OUTFITS not in VALID_INPUT:
                raise ValueError
            break
        except ValueError:
            print("Please only input yes or no.")
    return USER_POINTS, HAS_ALL_OUTFITS

def find_total_points(USER_POINTS, HAS_ALL_OUTFITS):
    # Gets a list of outfits the user owns if they don't have every outfit and calculates the total points
    total_points = 0
    if HAS_ALL_OUTFITS == "no":
        OUTFIT_HELP_MESSAGE = """
        We're going to enter the name of every outfit you have one by one now,
        Please type in the outfit name as it appears in the outfit inventory.
        When you are done typing in your outfits please type 'done'
        You can also type 'done' to skip this but doing so will give you an inaccurate level
        """
        print(OUTFIT_HELP_MESSAGE)
        outfit_inventory = []
        while True:
            current_outfit = capwords(input("Please input an outfit: "))
            if current_outfit == "Done":
                break
            if current_outfit not in master_outfits_dict:
                print(f"Could not find {current_outfit}, did you make a typo? ")
                continue
            if current_outfit in outfit_inventory:
                print("You already typed that one.")
                continue
            outfit_inventory.append(current_outfit)
    else:
        outfit_inventory = master_outfits_dict.keys()
    
    for outfit in outfit_inventory:
        total_points += master_outfits_dict[outfit]
    total_points += USER_POINTS
    return total_points

if __name__ == "__main__":
    main()