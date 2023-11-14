from src.game_logic import new_match


def main():
    bank = 1000
    choice = 1
    print("Welcome! Let's play blackjack! Your initial bank is 1000")
    while choice != '0':
        result, updated_bank = new_match(bank)
        bank = updated_bank
        print(f"Match result is {result}")
        print(f"Your current bank is {bank}")
        if bank == 0:
            print("Sorry, no more money left. Better luck next time!")
            break
        choice = input("Type 0 to exit, anything else to play again! \n")
    print(f"Final score is {bank}, gg")


if __name__ == "__main__":
    main()
