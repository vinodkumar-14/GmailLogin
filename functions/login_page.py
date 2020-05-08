__author__ = 'vinodkumar14'

from utils import test_base
from utils.settings import *

from IPython import embed
import logging

LOGGER = logging.getLogger(LOG_NAME)


def login_into_gmail(driver, username, password):

	driver.maximize_window()

	driver.implicitly_wait(IMPLICITLY_WAIT)

	test_base.get(driver, APP_URL)

	if driver.title.lower().strip() == 'sign in – google accounts' or \
		driver.title.lower().strip() == 'gmail':

		test_base.send_keys_using_xpath_locator(driver, "//input[@id='identifierId']", username)

		test_base.click_using_xpath(driver, "//span[@class='RveJvd snByac']")

		invalid_email_id = test_base.get_text_using_xpath(driver, "//div[@class='o6cuMc']")

		if invalid_email_id == INVALID_EMAIL_ID:
			LOGGER.info("Invalid Email ID Provided.")
			driver.save_screenshot(os.path.join(SCREENSHOTS, 'invalid_email_id.png'))

			return False

		else:

			test_base.send_keys_using_xpath_locator(driver, "//input[@name='password']", password, display_value=False)

			test_base.click_using_xpath(driver, "//span[contains(text(),'Next')]")

			wrong_pwd_xpath = "//span[contains(text(),'Wrong password. Try again or click Forgot password')]"
			wrong_pwd = test_base.get_text_using_xpath(driver, wrong_pwd_xpath)

			# To validate whether the user has entered wrong password
			if wrong_pwd == WRONG_PASSWORD:
				LOGGER.info("Incorrect Password Entered. Please Check the Username and Password.")
				driver.save_screenshot(os.path.join(SCREENSHOTS, 'incorrect_pwd.png'))

				return False

			else:
				recent_pwd_xpath = "//span[contains(text(),'Your password was changed less than an hour ago')]"
				recent_pwd_change = test_base.get_text_using_xpath(driver, recent_pwd_xpath)

				# To validate whether the user the recently the changed the password, but still entering old password
				if recent_pwd_change == RECENT_PASSWORD_CHANGE:
					LOGGER.info("Your password was changed less than an hour ago")
					driver.save_screenshot(os.path.join(SCREENSHOTS, 'pwd_changed.png'))

					return False

				else:
					txt_xpath = '//span[contains(text(), "Couldn\'t sign you in")]'
					txt_value = test_base.get_text_using_xpath(driver, txt_xpath)

					# Because of the Google restriction of low secure apps permission to login into Google account.
					if txt_value == COULDNOT_SIGN_IN:
						LOGGER.error("Coudn't sign you in Google Account")
						driver.save_screenshot(os.path.join(SCREENSHOTS, 'cannot_sign_in.png'))

						LOGGER.info("Hence, Finding alternative way to login into the Google Account")

						return alternative_gmail_login(driver, username, password)

					else:
						return login_verification(driver)

	else:
		LOGGER.info("Title of the Login webpage didn't match. Please investiage.")
		driver.save_screenshot(os.path.join(SCREENSHOTS, 'title_mismtach.png'))

		return False


def alternative_gmail_login(driver, username, password):
	""" Google has place restriction to test automated b """
	# found solution at: https://www.youtube.com/watch?v=HkgDRRWrZKg&feature=youtu.be

	test_base.get(driver, "https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")

	test_base.click_using_xpath(driver, "//*[@id='openid-buttons']/button[1]")

	test_base.send_keys_using_xpath_locator(driver, "//input[@type='email']", username)

	test_base.click_using_xpath(driver, '//*[@id="identifierNext"]')

	test_base.send_keys_using_xpath_locator(driver, '//input[@type="password"]', password, display_value=False)

	test_base.click_using_xpath(driver, '//*[@id="passwordNext"]')

	return login_verification(driver)



def login_verification(driver):
	try:
		test_base.get(driver, "https://www.gmail.com") 

		txt_value = test_base.get_text_using_xpath(driver, "//a[contains(text(),'Inbox')]")

		if txt_value.lower().strip() == 'inbox':
			LOGGER.info("Login into Gmail Account Successfully.")
			driver.save_screenshot(os.path.join(SCREENSHOTS, 'login_success.png'))

			return True
		else:
			LOGGER.info("FAILED to login into Gmail Account. Please investiage")
			driver.save_screenshot(os.path.join(SCREENSHOTS, 'login_fail.png'))
			
			return False
	except Exception as e:
		LOGGER.exception("login_verification() | Exception: %s"%(e))
		driver.save_screenshot(os.path.join(SCREENSHOTS, 'login_fail.png'))
		raise Exception(str(e))
