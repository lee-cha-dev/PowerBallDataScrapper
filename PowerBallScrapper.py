import time
import pickle
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class PowerBallScrapper(object):
    webpageNum = 1
    numRange = 1
    dataList = []
    counter = 1
    lastPage = False
    myURL = f'https://www.usamega.com/powerball/results/'
    options = webdriver.FirefoxOptions()
    driver = None

    def __init__(self):
        self.options.add_argument('-headless')

    def getPowerBallDataNotHeadless(self):
        # RESET VARIABLES
        self.webpageNum = 1
        self.numRange = 1
        self.dataList = []
        self.counter = 1
        self.lastPage = False

        while self.lastPage is False:
            self.myURL = f'https://www.usamega.com/powerball/results/{self.webpageNum}'
            self.driver = webdriver.Firefox(options=self.options)
            # self.driver.maximize_window()
            # time.sleep(1)

            self.driver.get(self.myURL)
            # time.sleep(5)

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
                print(f"Current Draw: {currentDraw}")
                self.dataList.append(currentDraw)
                if self.webpageNum == 124:
                    # PAGE 124 DEVIATES FROM THE OTHER PAGES
                    if self.counter == 21:
                        self.counter = 27
                    else:
                        self.counter += 1
                else:
                    self.counter += 1

            self.counter = 1
            print(f'Dataset size: {len(self.dataList)}')

            # CHECK FOR LAST PAGE
            try:
                nextButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/p/span/a[2]')
            except NoSuchElementException:
                if self.webpageNum > 1:
                    print('Last Page Found')
                    self.lastPage = True

            self.driver.close()
            self.webpageNum += 1



        print(f'End of Session dataList: {self.dataList}')

        # SAVE
        pickleOut = open("powerBallDataset", "wb")
        pickle.dump(self.dataList, pickleOut)
        pickleOut.close()
