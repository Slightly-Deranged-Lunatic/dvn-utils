def main():
    STARTING_LEVEL, ENDING_LEVEL = get_levels()
    EXP_SUM = 0
    for i in range(STARTING_LEVEL, ENDING_LEVEL):
         EXP_SUM += i*1000
    print(f"The total amount of EXP to go from {STARTING_LEVEL} to {ENDING_LEVEL} is {EXP_SUM}.")
    input("Press enter to close")

def get_levels():
    while True:
            try:
                STARTING_LEVEL = int(input("What level are we starting from? "))
                break
            except ValueError:
                print("Please only put a number in.")
    while True:
            try:
                ENDING_LEVEL = int(input("Enter the ending level. "))
                break
            except ValueError:
                print("Please only put a number in.")
    if STARTING_LEVEL > ENDING_LEVEL:
         print("Please make sure the starting level is less than the ending number.")
         STARTING_LEVEL, ENDING_LEVEL = get_levels()

    return STARTING_LEVEL, ENDING_LEVEL

if __name__ == "__main__":
    main()