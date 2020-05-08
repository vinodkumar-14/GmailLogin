
from logging.config import dictConfig
import logging
import os

APP_URL = "https://accounts.google.com/"
LOG_NAME = 'signzy_logs'
BROWSER = 'firefox'
HEADLESS = True

IMPLICITLY_WAIT = 10
PAGE_LOAD_TIMEOUT = 30
WEBDRIVER_WAIT = 30

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS = os.path.join(BASE_DIR, 'screenshots')

# For Ubuntu/Linux
GECKODRIVER_PATH = '/usr/bin/geckodriver'

# For windows OS - update the path or place inside signy_assignment folder
# GECKODRIVER_PATH = os.path.join(BASE_DIR, 'geckodriver.exe')

if not os.path.exists(SCREENSHOTS):
    os.mkdir(SCREENSHOTS)

## ERROR MESSAGE
INVALID_EMAIL_ID = "Couldn't find your Google Account"
COULDNOT_SIGN_IN = "Couldn't sign you in"
WRONG_PASSWORD = "Wrong password. Try again or click Forgot password to reset it."
RECENT_PASSWORD_CHANGE = "Your password was changed less than an hour ago"

## Logger Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, LOG_NAME + '.log'),
            # 'mode': 'a'
        }
    },

    'loggers': {
        LOG_NAME: {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

dictConfig(LOGGING)
logger = logging.getLogger(LOG_NAME)

