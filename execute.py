__author__ = 'vinodkumar14'

from functions import login_page, inbox
from utils import test_base
from utils.settings import *

import logging

LOGGER = logging.getLogger(LOG_NAME)


INPUT = [{
			"email": "email_id",
			"password": "password",
			"nth_email": 1,
		}, {
			"email": "email_id",
			"password": "password",
			"nth_email": 1,
		}]


def execute(email_id, password, nth_email):
	driver = test_base.activate_driver()

	try:
		if login_page.login_into_gmail(driver, email_id, password):

			inbox.select_primary_tab(driver)

			inbox.get_sender_name_and_subject_of_email_from_first_50_emails(driver, nth_email=nth_email)

	except:
		raise Exception("Some error during execution. Please investiage.")

	finally:
		test_base.close_driver(driver)


if __name__ == '__main__':

	for index, data in enumerate(INPUT):
		LOGGER.info("************** Test Data Set: %s Started *******************"%(index + 1))
		execute(data['email'], data['password'], data['nth_email'])
		LOGGER.info("************** Test Data Set: %s Completed *******************"%(index + 1))

