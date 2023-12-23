# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from selenium.webdriver.common.by import By


class LoadCategory:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def _load_category(self):
        try:
            category_list = self.driver.find_elements(by=By.XPATH, value=f"//*[contains(@class, 'main')]/a")
        except:
            return False

        return category_list

    def load_category(self):
        category_list = self._load_category()

        return category_list
