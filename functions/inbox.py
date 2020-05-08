__author__ = 'vinodkumar14'

from utils.settings import *
from utils import test_base

from IPython import embed
import logging

LOGGER = logging.getLogger(LOG_NAME)


def select_primary_tab(driver):
	""" Function to verify whether the Primary Tab is selected or not """
	primary_tab_xpath = "//table[@class='aKk']//tbody//tr[@role='tablist']//td[1]//div[@aria-label='Primary']"
	if test_base.get_attribure(driver, primary_tab_xpath, 'aria-selected') == 'true':
		LOGGER.info("By default, Primary Tab is selected after login into gmail.")

	else:
		LOGGER.info("Primary Tab isn't selected by default, hence selected Primary tab")

		test_base.click_using_xpath(driver, primary_tab_xpath)


def get_sender_name_and_subject_of_email_from_first_50_emails(driver, nth_email=1):
	""" Function to return sender name and subject of the email """
	try:
		tbl_xpath = "//div[@class='UI']//div[3]//table//tr"
		tot_emails = len(driver.find_elements_by_xpath(tbl_xpath))

		if tot_emails > 0 and tot_emails <= 50:

			sender_xpath = "%s[%s]//td[@class='yX xY ']//div[2]//span//span[1]"%(tbl_xpath, nth_email)
			sender_name = driver.find_element_by_xpath(sender_xpath).text

			subject_xpath = "%s[%s]//span[@class='bog']//span"%(tbl_xpath, nth_email)
			email_subject = driver.find_element_by_xpath(subject_xpath).text

			LOGGER.info("********************************************")
			LOGGER.info("Sender Name: %s"%(sender_name))
			LOGGER.info("Email Subject: %s"%(email_subject))
			LOGGER.info("********************************************")

			driver.save_screenshot(os.path.join(SCREENSHOTS, 'output_info.png'))

		elif tot_emails > 50:
			LOGGER.info("Please try provide nth email less than 50. ")

	except Exception as e:
		LOGGER.exception(str(e))
		driver.save_screenshot(os.path.join(SCREENSHOTS, 'output_error.png'))
		raise Exception("Exception while getting sender name and subject of the email.")

