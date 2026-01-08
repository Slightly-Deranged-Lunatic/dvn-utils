import outfits_cost
outfits = outfits_cost.outfits

<<<<<<< HEAD:points_to_levels.py/points_to_levels.py
def points_to_levels():
=======
def main():
    OUTFITS_SUM = sum(outfits.values())
>>>>>>> parent of 506c1a0 (Let the user input outfits they have just in case they don't have every outfit.):Points To Levels/main.py
    USER_POINTS, HAS_ALL_OUTFITS = get_user_input()
    if HAS_ALL_OUTFITS == "yes":
        total_points = USER_POINTS + OUTFITS_SUM
    else:
        total_points = USER_POINTS

    level = 1
    print(f"Total points before looping is {total_points}")
    while True:
        level += 1
        total_points -= level * 2
        if total_points <= 0:
            level -= 1
            total_points += level * 2
            break
    print(f"Your level given your points would be {level} with {total_points} points leftover.")

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

if __name__ == "__main__":
    points_to_levels()