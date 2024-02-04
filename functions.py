from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from utils import *
from time import sleep    
from selenium.webdriver.chrome.service import Service

def initializeSelenium():
    # Load options
    chrome_options = Options()
    #chrome_options.add_argument("user-data-dir=/tmp/profile") 
    #chrome_options.add_argument("log-level=1")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    chrome_options.add_argument("--headless=new")
    service = Service(executable_path='drivers/chromedriver')
    return webdriver.Chrome(service=service,options=chrome_options)

def initializeZupass(driver, findElements, email, password):
    findElements.element_exist_xpath('//*[@placeholder]').send_keys(email) # Insert amount
    findElements.element_exist_xpath('//button[text()="Continue"]').click() # Continue button
    findElements.element_exist_xpath('//*[@placeholder="Password"]').send_keys(password) # Password button
    findElements.element_exist_xpath('//button[text()="Login"]').click() # Continue button
    availableNow = findElements.element_exist_xpath('//img[@src="/images/frogs/pixel_frog.png"]').click()
    sleep(15)

def getFrogs(driver, findElements):
    findElements.element_exist_xpath('//*[contains(text(), "search SWAMP")]').click() # Confirm Button
    # findElements.element_exist_xpath('//*[contains(text(), "search CELESTIAL POND")]').click() # Confirm Button
    # findElements.element_exist_xpath('//*[contains(text(), "search THE CAPITAL")]').click() # Confirm Button
    # findElements.element_exist_xpath('//*[contains(text(), "search JUNGLE")]').click() # Confirm Button
    # findElements.element_exist_xpath('//*[contains(text(), "search DESERT")]').click() # Confirm Button
    # findElements.element_exist_xpath('//*[contains(text(), "search THE WRITHING VOID")]').click() # Confirm Button
    sleep(5)
