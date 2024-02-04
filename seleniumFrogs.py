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

emailList = []
password = ""

## get frogs
while True:
    for email in emailList:
        driver = initializeSelenium()
        try:
            # Load find elements with the default wait
            defualtWaitSeconds = 15
            defaultWaitObject = WebDriverWait(driver, defualtWaitSeconds)
            findElementsInstance = findElements(defaultWaitObject)
            driver.get("https://zupass.org/#/login")

            ###################
            # Load ZuPass   #
            ###################
            initializeZupass(driver, findElementsInstance, email, password)

            getFrogs(driver, findElementsInstance)
            print("Wait for next hunt")
            sleep(40)
            driver.quit()
        except:
            driver.quit()

    sleep(60*15)

