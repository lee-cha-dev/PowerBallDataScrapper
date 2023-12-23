from PowerBallScrapper import PowerBallScrapper
from Tests.PowerBallScrapperTest import PowerBallScrapperTest

if __name__ == '__main__':
    # RUN TESTS
    tester = PowerBallScrapperTest()
    tester.startTests()

    # RUN DATA SCRAPPER
    t = PowerBallScrapper()
    t.getPowerBallDataHeadless()
