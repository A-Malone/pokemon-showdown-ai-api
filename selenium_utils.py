from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

import time

def fresh_find(root, EC, timeout=2, retries=10):
    for i in range(retries):
        try:
            elem = WebDriverWait(root, timeout).until(EC)
            elem.is_enabled()
            return elem
        except StaleElementReferenceException:
            print('attempting to recover from StaleElementReferenceException...')
            time.sleep(0.25)
    raise StaleElementReferenceException("All {} tries yielded stale elements".format(retries))
