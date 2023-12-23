import time
import pickle
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class PowerBallScrapper(object):
    myURL = 'https://www.usamega.com/powerball/results/1'

    webpageNum = 1
    stillWorking = True
    numRange = 1
    dataList = []
    counter = 1
    lastPage = False

    def __init__(self):
        pass

    def getPowerBallDataNotHeadless(self):
        # RESET VARIABLES
        self.webpageNum = 131
        self.stillWorking = True
        self.numRange = 1
        self.dataList = []
        self.counter = 1

        drawingOnPage = 0

        while self.lastPage is False:
            myURL = f'https://www.usamega.com/powerball/results/{self.webpageNum}'
            driver = webdriver.Firefox()
            driver.maximize_window()
            time.sleep(1)

            driver.get(myURL)
            time.sleep(5)

            drawingsOnPage = len(driver.find_elements(By.XPATH, f'/html/body/div[1]/main/div[4]/table/tbody/tr'))
            # WORKS THROUGH ALL DRAWINGS ON THAT PAGE
            while self.counter - 1 < drawingsOnPage:
                currentDraw = []
                while self.numRange < 7:
                    numData = driver.find_element(By.XPATH,
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
                nextButton = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/p/span/a[2]')
            except NoSuchElementException:
                print('Last Page Found')
                self.lastPage = True
            
            driver.close()
            self.webpageNum += 1



        print(f'End of Session dataList: {self.dataList}')

        # SAVE
        pickleOut = open("powerBallDataset", "wb")
        pickle.dump(self.dataList, pickleOut)
        pickleOut.close()


t = PowerBallScrapper()
t.getPowerBallDataNotHeadless()

