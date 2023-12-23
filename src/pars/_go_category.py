# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from settings import main_category


class GoCategory:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.main_category_list = settings['main_category_list']

    def _click_category(self, row_category):
        try:
            row_category.click()
        except:
            return False

        time.sleep(1)

        return True

    def get_title(self, row_category):
        try:
            title = row_category.get_attribute('title')
        except:
            return False

        time.sleep(1)

        return title

    def go_category(self):
        row_category = self.main_category_list[main_category]

        title = self.get_title(row_category)

        res_click = self._click_category(row_category)

        return title
