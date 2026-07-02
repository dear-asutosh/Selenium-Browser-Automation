# 1. How to navigate Browser
#     a.Opening a browser : we already did this in the last example
#     b.Navigating URLs


#import webdriver module from selenium package
from selenium import webdriver
import time
#instantiate webdriver and launch Chrome browser
driver=webdriver.Chrome()

#Navigate to google - open URL
driver.get("https://www.google.com")
time.sleep(2) #wait for 2 seconds to let the page load
#Navigate to youtube - open URL
driver.get("https://www.youtube.com")
time.sleep(2)

#go back to google
driver.back()
time.sleep(2)

#go forward to youtube
driver.forward()
time.sleep(2)

#refresh the current page
driver.refresh()
time.sleep(2)

#close the browser window
driver.quit()