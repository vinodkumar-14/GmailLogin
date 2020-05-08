__author__ = 'vinodkumar14'

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from IPython import embed
import logging

from utils.settings import *

LOGGER = logging.getLogger(LOG_NAME)

def activate_driver():  
    try:
        if BROWSER.lower().strip() == 'chrome':
            options = webdriver.ChromeOptions()

            if HEADLESS:
                options.add_argument('--headless')

            desired_capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
            desired_capabilities.update(options.to_capabilities())
            driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
            
            LOGGER.info("Chrome Webdriver is initiated successfully!")

            return driver

        if BROWSER.lower().strip() == 'firefox':
            options = webdriver.FirefoxOptions()

            if HEADLESS:
                options.headless = True

            desired_capabilities = {'browserName': 'firefox', 'javascriptEnabled': True}
            desired_capabilities.update(options.to_capabilities())

            driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH, desired_capabilities=desired_capabilities)
            
            LOGGER.info("Firefox Webdriver is initiated successfully!")

            return driver

    except Exception as e:
        LOGGER.exception("Test Base | activate_driver() | Exception: %s"%(e))
        raise Exception("Error is initializing the webdriver. Please Investigate")


def get(driver, url):
    """ Functionality to open the URL of an application """
    try:
        driver.get(url)
        LOGGER.info("Driver has loaded URL: '%s' web-page in the current browser session.", url)

        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    except Exception as e:
        LOGGER.exception("Test Base | get() | Exception: %s"%(e))


def close_driver(driver):
    """ Functionality to close the web browser and clear the cookies """
    try:
        driver.delete_all_cookies()
        driver.quit()
        LOGGER.info("Web Driver has cleared cookies and closed the browser")
    except Exception as e:
        LOGGER.exception("Test Base | close_driver() | Exception: %s"%(e))



def send_keys_using_xpath_locator(driver, xpath_value, value, display_value=True):
    """ Functionality to send keys/values to the web element on the web page """
    try:
        send_element = WebDriverWait(driver, WEBDRIVER_WAIT).until(EC.visibility_of_element_located((By.XPATH, xpath_value)))

        driver.find_element_by_xpath(xpath_value).send_keys(str(value))

        if display_value:
            LOGGER.info("Driver has typed '%s' into web-lement.", value)
        else:
            LOGGER.info("Driver has typed '%s' into web-lement.", ''.join([''.join('*') for i in range(len(value))]))
    except Exception as e:
        LOGGER.exception("Test Base | send_keys_using_xpath_locator() | Exception: %s"%(e))


def click_using_xpath(driver, xpath_value):
    """ Functionality to perform click on the web element on the web page """
    try:
        click_element = WebDriverWait(driver, WEBDRIVER_WAIT).until(EC.element_to_be_clickable((By.XPATH, xpath_value)))
        click_element.click()
        LOGGER.info("Driver clicked on web-element.",)
    except:
        try:
            driver.execute_script("arguments[0].click();", click_element)
            LOGGER.info("Driver clicked on web-element using JavaScript Execute.",)
        except Exception as e:
            LOGGER.exception("Test Base | click_using_xpath() | Exception: %s"%(e))


def get_text_using_xpath(driver, xpath_value, can_fail=True):
    try:
        WebDriverWait(driver, WEBDRIVER_WAIT).until(EC.visibility_of_element_located((By.XPATH, xpath_value)))
        element_value = driver.find_element_by_xpath(xpath_value).text
        LOGGER.info("Text '%s' is found for the web-element"%(element_value))

        return element_value
    except Exception as e:
        if can_fail:
            LOGGER.info("Text Webdriver was looking for, couldn't be found.")
        else:
            LOGGER.exception("Test Base | get_text_using_xpath() | Exception: %s"%(e))

        return ''


def get_attribure(driver, xpath_value, attribute_name):
    try:
        WebDriverWait(driver, WEBDRIVER_WAIT).until(EC.visibility_of_element_located((By.XPATH, xpath_value)))

        return driver.find_element_by_xpath(xpath_value).get_attribute(attribute_name)
    except Exception as e:
        LOGGER.exception("Test Base | get_attribure() | Exception: %s"%(e))

