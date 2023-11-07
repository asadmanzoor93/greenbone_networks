import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""
security
"""

ALLOWED_HOSTS = ['*']
DEBUG = True

"""
urls
"""

BASE_URL = 'http://localhost:8000'

SITE_ID = 'localhost'

MESSAGING_SERVICE_URL = "http://localhost:8080/api/notify"
