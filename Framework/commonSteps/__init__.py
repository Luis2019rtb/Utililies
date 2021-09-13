##############
# Common steps using webdriver
###############
import time
# Handling utilities from selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

# Getting web driver manager instance
from webdriver_manager.chrome import ChromeDriverManager

## ------ Basic Actions ----- ###
# =========================== #

# Automatic chrome driver manager


def getAutomaticChromeDriver():
    chromeOption = Options()
    chromeOption.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(ChromeDriverManager().install(), options=chromeOption)


###
# Perform click on a webelement
##


def clickingOn(webElement):
    print("Clikcing on ==> " + str(webElement))
    try:
        return webElement.click()
    except Exception as e:
        print("Error occour when cliking on ==> "+str(webElement))


#  Searching web element on the page by
#   using the current driver and the xpath given


def getWebElement(driver, xpath):
    print("Searching xpath =>" + str(xpath))
    for times in range(0, 2):
        try:
            time.sleep(1)
            return driver.find_element_by_xpath(
                xpath
            )
        except StaleElementReferenceException as e:
            pass
        break

    raise Exception('Driver object not finding ' + str(xpath))

#  Searching web element on the page by
#   using the current driver and the xpath given


def getWebElements(driver, xpath):
    print("Searching several elements xpath =>" + str(xpath))
    for times in range(0, 2):
        try:
            time.sleep(1)
            return driver.find_elements_by_xpath(
                xpath
            )
        except StaleElementReferenceException as e:
            pass
    raise Exception('Driver object not finding ' + str(xpath))

# Accessing a web page


def accessingToUrl(driver, url):
    try:
        print("Accessing to " + str(url))
        time.sleep(1)
        driver.get(url)
        print("Maximazing windows")
        driver.maximize_window()
        return driver
    except Exception as e:
        print("Error accesing to the pase " + str(e))


# Initiated driver
def initiateChromeWebDriver(driverPath):
    print("Initiating driver")
    try:
        currentDriver = webdriver.Chrome(driverPath)
        return currentDriver
    except Exception as e:
        print("Error initiating driver ==> " + str(e))


def clearAndWrite(webElement, keys):
    print("Sending keys to ==> " + str(webElement))
    try:
        webElement.clear()
        return webElement.send_keys(keys)
    except Exception as e:
        print("Error occour when trying to locate ==> "+str(webElement))
