# cell[0]
!pip install selenium

# cell[1]
import time
from selenium import webdriver

driver = webdriver.Chrome()


def openPage(page, keep=False):
    driver.get(page)
    if keep:
        time.sleep(3600)

# cell[2]
openPage("https://twitter.com/")
