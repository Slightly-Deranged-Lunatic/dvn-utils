import importlib
def main():
    while True:
        try:
            wave_to_output = int(input("What wave would you like to view? "))
        except ValueError:
            print("Your wave has to be a whole number.")
            continue
        if wave_to_output > 11 or wave_to_output < 1:
            print("Your wave cannot be greater than 11 or less than 1.")
            continue
        break
    while True:
        player_count_or_multiplier = input('Are you going to give a player count or unit multiplier? Type "player count" for player count, and "unit multiplier" for unit multiplier. ')
        if player_count_or_multiplier == "player count":
            while True:
                try:
                    unit_multiplier_as_players = int(input("What is the player count? "))
                except ValueError:
                    print("Your player count wasn't a whole number. Please try again")
                    continue
                if unit_multiplier_as_players < 0:
                    print("Your player count cannot be less than 0")
                    continue
                break
            unit_multiplier_as_multiplier = 1
            for player in range(unit_multiplier_as_players):
                unit_multiplier_as_multiplier += 0.25
            break
        elif player_count_or_multiplier == "unit multiplier":
            while True:
                try:
                    unit_multiplier_as_multiplier = float(input("What is the multiplier, given as a decimal or whole number? "))
                except ValueError:
                    print("Your unit multiplier wasn't a whole number or floating point")
                    continue
                break
        else:
            print("What you wanted to provide wasn't an option.")
    print("meow")
main()