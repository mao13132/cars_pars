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
from selenium.webdriver.common.keys import Keys

from src.pars.get_all_rows import get_all_rows


class LoadFullRow:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def scroll_down(self):
        self.driver.find_element(by=By.XPATH, value=f"//body").click()

        for _try in range(2):
            self.driver.find_element(by=By.XPATH, value=f"//body").send_keys(Keys.END)

            time.sleep(1)

    def loop_load_full_rows(self):
        while True:
            rows = get_all_rows(self.driver)

            start_count_row = len(rows)

            self.scroll_down()

            time.sleep(2)

            rows = get_all_rows(self.driver)

            end_count_row = len(rows)

            if start_count_row != end_count_row:
                continue

            return end_count_row
