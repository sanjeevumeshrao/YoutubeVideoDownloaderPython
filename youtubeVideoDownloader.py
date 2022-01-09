from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "./downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

# import requests
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

file1 = open('urls.txt', 'r') #text file of youtube urls. Line separated
urls = file1.readlines()

from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.folderList", 1)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", "./Downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4")

for url in urls:
    try:
        driver = webdriver.Firefox(executable_path="/Users/sanjeev/Downloads/geckodriver", options=options)
        driver.get("https://yt1s.com/en90/youtube-to-mp4")

        inputElement = driver.find_element_by_id("s_input")
        inputElement.send_keys(url)
        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)
        inputElement = driver.find_element_by_id("btn-action")
        inputElement.click()
        time.sleep(10)

        # time.sleep(10)
        inputElement = driver.find_element_by_id("asuccess")
        inputElement.click()
        time.sleep(300)  #wait 5 minutes to download
        print("closing....")
        driver.quit()
    except:
        print("Error in url: "+ url)


