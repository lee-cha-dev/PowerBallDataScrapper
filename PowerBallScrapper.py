import time
import pickle
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import shutil


def cls():
    os.system('cls')


class PowerBallScrapper(object):
    webpageNum = 1
    numRange = 1
    dataList = []
    counter = 1
    lastPage = False
    myURL = f'https://www.usamega.com/powerball/results/'
    options = webdriver.FirefoxOptions()
    driver = None
    columns = shutil.get_terminal_size().columns

    def __init__(self):
        self.options.add_argument('-headless')

    def getPowerBallDataHeadless(self):
        # RESET VARIABLES
        self.webpageNum = 1
        self.numRange = 1
        self.dataList = []
        self.counter = 1
        self.lastPage = False

        print("Starting Up Miner...\n")
        while self.lastPage is False:
            self.columns = shutil.get_terminal_size().columns  # UPDATES THE COLUMN SIZE IN CASE USER RESIZES

            cls()
            print("".center(self.columns, '-'))
            print(" Miners At Work ".center(self.columns, '*'))
            print("".center(self.columns, '-'))
            print("Mining Data from Page {}".format(self.webpageNum).center(self.columns))

            self.myURL = f'https://www.usamega.com/powerball/results/{self.webpageNum}'
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.myURL)

            drawingsOnPage = len(self.driver.find_elements(By.XPATH, f'/html/body/div[1]/main/div[4]/table/tbody/tr'))
            # WORKS THROUGH ALL DRAWINGS ON THAT PAGE
            while self.counter - 1 < drawingsOnPage:
                currentDraw = []
                while self.numRange < 7:
                    numData = self.driver.find_element(By.XPATH,
                                                       f'/html/body/div[1]/main/div[4]/table/tbody/tr[{self.counter}]/td[1]/section/ul/li[{self.numRange}]')
                    drawNum = numData.get_property("innerHTML")
                    currentDraw.append(int(drawNum))
                    self.numRange += 1
                self.numRange = 1
                self.dataList.append(currentDraw)
                self.counter += 1
            self.counter = 1

            # CHECK FOR LAST PAGE
            try:
                nextButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/p/span/a[2]')
            except NoSuchElementException:
                if self.webpageNum > 1:
                    print('Last Page Found'.center(self.columns))
                    self.lastPage = True
            self.driver.close()
            self.webpageNum += 1

        print()
        print(f'Shutting Down Miner..'.center(self.columns))
        print()
        print(' End of Session '.center(self.columns, '*'))
        print()

        # SAVE
        pickleOut = open("powerBallDataset", "wb")
        pickle.dump(self.dataList, pickleOut)
        pickleOut.close()
