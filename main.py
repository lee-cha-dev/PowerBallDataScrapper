from PowerBallScrapper import PowerBallScrapper
from Tests.PowerBallScrapperTest import PowerBallScrapperTest
import shutil


def handle_user_input():
    columns = shutil.get_terminal_size().columns
    valid_input = False
    user_input = ""
    while not valid_input:
        user_input = input("Start Up the Miner?: y or n or q (for quit)\n".center(columns))
        if user_input.lower() == 'y' or user_input.lower() == 'q':
            valid_input = True
        elif user_input.lower() == 'n':
            print("Miners Are Standing By!".center(columns))
    if user_input.lower() != 'q':
        # RUN DATA SCRAPPER
        t = PowerBallScrapper()
        t.getPowerBallDataHeadless()


if __name__ == '__main__':
    # RUN TESTS
    tester = PowerBallScrapperTest()
    tester.startTests()

    handle_user_input()
