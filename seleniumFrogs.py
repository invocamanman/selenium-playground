from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep    
from utils import *
from functions import *
import sys
# virtual display
#from pyvirtualdisplay import Display
# for arg in sys.argv:
#     if arg.lower() == "server":
#         display = Display(visible=0, size=(1920, 1080))
#         display.start()

###################
# Load selenium  #
###################

emailList =  ["youremail1@gmail.com", "youremail2@gmail.com"]
passwordList = ["yourpassword1", "yourpassword2"]

## get frogs
while True:
    for email, password in zip(emailList, passwordList):
        driver = initializeSelenium()
        try:
            # Load find elements with the default wait
            defualtWaitSeconds = 15
            defaultWaitObject = WebDriverWait(driver, defualtWaitSeconds)
            findElementsInstance = findElements(defaultWaitObject)
            driver.get("https://zupass.org/#/?folder=FrogCrypto")

            ###################
            # Load ZuPass   #
            ###################
            initializeZupass(driver, findElementsInstance, email, password)

            ###################
            # Mine Frogs   #
            ###################
            getFrogs(driver, findElementsInstance)
            print("Wait for next hunt")
            sleep(40)
            driver.quit()
        except:
            driver.quit()

    sleep(60*15)

