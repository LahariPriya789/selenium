from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://ackodrive.com/cars/'
driver.get(url)
time.sleep(5)      #open browser for 5 sec
driver.maximize_window()   # maximizes the window
time.sleep(3)
elemet = driver.find_element(by=By.XPATH, value = '//*[@id="__next"]/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/a[1]')    # click bangalore automatically
elemet.click()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")         #scroll to bottom of page
time.sleep(60*5)   #open browser for 5 min   60sex*5
