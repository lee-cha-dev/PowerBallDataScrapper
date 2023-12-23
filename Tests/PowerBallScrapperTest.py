from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from PowerBallScrapper import PowerBallScrapper


class PowerBallScrapperTest:
    scrapper = PowerBallScrapper()
    failMessages = []
    failToFindTable = False
    failToFindBody = False
    failToFindRow = False
    failToFindListOfDrawings = False
    failToFindDrawingNum = False

    def __init__(self):
        pass

    def findTable(self):
        # FIND THE TABLE THAT HOLD THE TBODY
        try:
            table = self.scrapper.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/table')
        except NoSuchElementException:
            self.failToFindTable = True
        finally:
            if self.failToFindTable:
                self.failMessages.append("Tests::Failed::Could NOT find the Table of drawings.")
            else:
                self.failMessages.append("Tests::Passed::Successfully found the Table of drawings.")

    def findTBody(self):
        # FIND THE TABLE BODY THAT HOLD ALL DRAWINGS
        try:
            body = self.scrapper.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/table/tbody')
        except NoSuchElementException:
            self.failToFindBody = True
        finally:
            if self.failToFindBody:
                self.failMessages.append("Tests::Failed::Could NOT find the the table body of drawings.")
            else:
                self.failMessages.append("Tests::Passed::successfully found the table body of drawings.")

    def findFirstTableRow(self):
        # FIND THE FIRST TABLE ROW WITH THE FIRST DRAWING
        try:
            row = self.scrapper.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/table/tbody/tr[1]')
        except NoSuchElementException:
            self.failToFindRow = True
        finally:
            if self.failToFindRow:
                self.failMessages.append("Tests::Failed::Could NOT find the first row of a drawing.")
            else:
                self.failMessages.append("Tests::Passed::Successfully found the first row of a drawing.")

    def findUnorderedList(self):
        # FIND THE UNORDERED LIST OF NUMBERS FOR THE FIRST DRAWING
        try:
            listOfDrawings = self.scrapper.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/table/tbody/tr[1]/td[1]/section/ul[1]')
        except NoSuchElementException:
            self.failToFindListOfDrawings = True
        finally:
            if self.failToFindListOfDrawings:
                self.failMessages.append("Tests::Failed::Could NOT find the unordered list of the drawings.")
            else:
                self.failMessages.append("Tests::Passed::successfully found the unordered list of the drawings.")

    def findFirstDrawingWithinUList(self):
        # FIND THE FIRST DRAWING WITHIN THE UNORDERED LIST
        try:
            drawingNum = self.scrapper.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/table/tbody/tr[1]/td[1]/section/ul[1]/li[1]')
        except NoSuchElementException:
            self.failToFindDrawingNum = True
        finally:
            if self.failToFindDrawingNum:
                self.failMessages.append("Tests::Failed::Could NOT find the first drawing")
            else:
                self.failMessages.append("Tests::Passed::successfully found the first drawing")

    def startTests(self):
        print("\n------------------------------------------------------------------------------------------------------")
        print("Tests::starting tests\n")

        # INIT INSTANCE
        self.scrapper.driver = webdriver.Firefox(options=self.scrapper.options)
        self.scrapper.myURL = f'https://www.usamega.com/powerball/results/1'

        # GET URL
        self.scrapper.driver.get(self.scrapper.myURL)

        # RUN TESTS
        self.findTable()
        self.findTBody()
        self.findFirstTableRow()
        self.findUnorderedList()
        self.findFirstDrawingWithinUList()

        # CLOSE DRIVER
        self.scrapper.driver.quit()

        for message in self.failMessages:
            print(message)

        print("\nTests::tests complete")
        print("------------------------------------------------------------------------------------------------------\n")
