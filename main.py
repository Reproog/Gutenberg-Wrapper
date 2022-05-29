from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

with open("Links.txt") as fp:
    Lines = fp.readlines()

curDir = os.path.abspath(os.getcwd())
folderName = "Downloads"
DownPath = os.path.join(curDir,folderName)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", DownPath)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

def Download():
    for line in Lines:
        Link = line.strip()
        print("{}".format(line.strip()))

        # Path to Driver
        s = Service("Driver\geckodriver.exe")
        driver = webdriver.Firefox(firefox_profile=profile,service=s)

        DownloadURL = "http://www.epub2go.eu"

        driver.get(DownloadURL)

        LinkField = driver.find_element_by_id("spiegelURL")
        LinkField.send_keys(Link)
        LinkField.send_keys(Keys.ENTER)

        time.sleep(5)

        Download = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/a")
        Download.click()

        driver.close()

if __name__ == "__main__":
    start = time.time()
    Download()
    end = time.time()

    Dur = str(end - start)
    print("")
    print("")
    print("")
    print("Successfully download")
    print(f"Duration: {Dur} seconds.")