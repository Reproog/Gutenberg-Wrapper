from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

curDir = os.path.abspath(os.getcwd())
folderName = "Downloads"
DownPath = os.path.join(curDir,folderName)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", DownPath)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")


# Path to Driver
s = Service("Driver\geckodriver.exe")
driver = webdriver.Firefox(firefox_profile=profile,service=s)

Link = "https://www.projekt-gutenberg.org/hugo/notreda1/notreda1.html"
DownloadURL = "http://www.epub2go.eu"


driver.get(DownloadURL)

LinkField = driver.find_element_by_id("spiegelURL")
LinkField.send_keys(Link)
LinkField.send_keys(Keys.ENTER)

time.sleep(1)

Download = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/a")
Download.click()

driver.close()
