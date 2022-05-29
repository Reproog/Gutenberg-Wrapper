from selenium import webdriver
from selenium.webdriver.common.keys import Keys


Link = "https://www.projekt-gutenberg.org/hugo/notreda1/notreda1.html"


DownloadURL = "epub2go.eu"
LinkField = driver.find_element_by_id("spiegelURL")
LinkField.send_keys(Link)
LinkField.send_keys(Keys.ENTER)
LinkField.submit()
 
DownloadButton =
driver.find_element_by_xpath("/html/body/div.wrapper/div#epub/div#ePubDLs/div#resultContainer0/a")

DownloadButton.click()


driver = webdriver.Firefox()



driver.quit()
