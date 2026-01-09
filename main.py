from exp_calculator.main import main as exp_calculator
from hell_wave_calculator.main import main as hell_wave_calculator
from points_to_levels.main import main as points_to_levels_calculator
import os

def main():
    while True:
        clear()
        choice = get_user_choice()
        if choice == 0:
            print("Bye bye!")
            raise SystemExit
        elif choice == 1:
            exp_calculator()
        elif choice == 2:
            hell_wave_calculator()
        elif choice == 3:
            points_to_levels_calculator()

def get_user_choice():
    CHOICE_TEXT = """Please make a choice between the below
    0) Quit the program
    1) EXP calculator (how much exp to go from one level to the next)
    2) Hell wave calculator (predict how many enemies will be in the given hell wave)
    3) Points to level calculator (how many levels you should have given your points)
    """
    while True:
        try:
            choice = int(input(CHOICE_TEXT ))
            if choice not in range(4):
                raise ValueError
            return choice
        except ValueError:
            print("Please only type a number 0 to 3")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()