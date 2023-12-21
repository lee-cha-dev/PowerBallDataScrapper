import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By


class PowerBallScrapper(object):
    myURL = 'https://www.usamega.com/powerball/results/1'

    webpageNum = 1
    stillWorking = True
    numRange = 1
    dataList = []
    counter = 1

    def __init__(self):
        pass

    def getPowerBallNotHeadless(self):
        # RESET VARIABLES
        webpageNum = 1
        stillWorking = True
        numRange = 1
        dataList = []
        counter = 1

        while self.webpageNum < 120:
            myURL = f'https://www.usamega.com/powerball/results/{self.webpageNum}'
            driver = webdriver.Firefox()
            driver.maximize_window()
            time.sleep(1)

            driver.get(myURL)
            time.sleep(5)

            while self.stillWorking:
                # WORKS THROUGH ALL DRAWINGS ON THAT PAGE
                while self.counter < 27:
                    currentDraw = []
                    while self.numRange < 7:
                        numData = driver.find_element(By.XPATH,
                                                      f'/html/body/div[1]/main/div[4]/table/tbody/tr[{self.counter}]/td[1]/section/ul[1]/li[{self.numRange}]')
                        drawNum = numData.get_property("innerHTML")
                        currentDraw.append(int(drawNum))
                        self.numRange += 1
                    self.numRange = 1
                    self.dataList.append(currentDraw)
                    if self.webpageNum == 124:
                        if self.counter == 13:
                            self.counter = 27
                        else:
                            self.counter += 1
                    else:
                        self.counter += 1

                self.counter = 1
                print(f'Dataset size: {len(self.dataList)}')

            driver.close()
            self.webpageNum += 1

        print(f'End of Session dataList: {self.dataList}')

        # SAVE
        pickleOut = open("powerBallDataset", "wb")
        pickle.dump(self.dataList, pickleOut)
        pickleOut.close()

