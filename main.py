from src.game_logic.game_logic import new_match
from src.logs import logger


def main():
    bank_value = 1000
    player_choice = 1
    logger.info("Welcome! Let's play blackjack! Your initial bank is 1000")
    while player_choice != '0':
        match_result, updated_bank = new_match(bank_value)
        bank_value = updated_bank
        logger.info(f"Match result is {match_result}")
        logger.info(f"Your current bank is {bank_value}")
        if bank_value == 0:
            logger.info("Sorry, no more money left. Better luck next time!")
            break
        player_choice = input("Type 0 to exit, anything else to play again! \n")
    logger.info(f"Final score is {bank_value}, gg")


if __name__ == "__main__":
    main()
