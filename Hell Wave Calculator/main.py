import importlib
import sys
import math

def main():
    wave_composition = get_wave()
    while True:
        player_count_or_multiplier = input('Are you going to give a player count or unit multiplier? Type "player count" for player count, and "unit multiplier" for unit multiplier. ')
        if player_count_or_multiplier == "player count":
            unit_multiplier = player_count_to_multiplier()
            break
        elif player_count_or_multiplier == "unit multiplier":
            unit_multiplier = input_to_multiplier()
            break
        else:
            print("What you provided wasn't an option.")
            continue
        break
    print_wave_comp(unit_multiplier, wave_composition)

def input_to_multiplier():
    # Lets the user define a multiplier themselves
    while True:
        try:
            unit_multiplier = float(input("What is the multiplier, given as a decimal or whole number? "))
        except ValueError:
            print("Your unit multiplier wasn't a whole number or floating point")
            continue
        return unit_multiplier

def get_wave():
    # Gets the wave as user input and imports the file for that wave
    VALID_WAVES = range(1, 12)
    while True:
        try:
            wave_to_output = int(input("What wave would you like to view? "))
            if wave_to_output not in VALID_WAVES:
                raise ValueError
        except ValueError:
            print("Your wave has to be a whole number between 1 and 11.")
            continue
        break
    sys.path.append("waves")
    wave_composition = importlib.import_module(f"wave_{wave_to_output}")
    return wave_composition

def player_count_to_multiplier():
    # Gets the player count and converts it to a multiplier
    while True:
        try:
            player_count = int(input("What is the player count? "))
            if player_count <= 0:
                raise ValueError
        except ValueError:
            print("Your player count wasn't a positive whole number. Please try again")
            continue
        break
    unit_multiplier = (player_count * 0.25) + 1
    return unit_multiplier

def print_wave_comp(unit_multiplier, wave_composition):
    # Prints the wave composition and total amount of units after accounting for unit multiplier
    total_unit_count = 0
    for unit, unit_count in wave_composition.composition.items():
        if unit == "Boss" or unit == "Ares":
            if unit == "Boss":
                total_unit_count += 9
            else:
                total_unit_count += 1
            print(f"{unit} x {unit_count}")
            continue
        unit_count = math.ceil(unit_count * unit_multiplier)
        total_unit_count += unit_count
        print(f"{unit} x {unit_count}")
    print(f"Total units: {total_unit_count}")

if __name__ == "__main__":
    main()