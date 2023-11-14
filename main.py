from src.game_logic import new_match
from src.logger_setup import global_logger as logger


def main():
    bank = 1000
    choice = 1
    logger.info("Welcome! Let's play blackjack! Your initial bank is 1000")
    while choice != '0':
        result, updated_bank = new_match(bank)
        bank = updated_bank
        logger.info(f"Match result is {result}")
        logger.info(f"Your current bank is {bank}")
        if bank == 0:
            logger.info("Sorry, no more money left. Better luck next time!")
            break
        choice = input("Type 0 to exit, anything else to play again! \n")
    logger.info(f"Final score is {bank}, gg")


if __name__ == "__main__":
    main()
