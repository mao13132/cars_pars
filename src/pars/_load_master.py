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

from src.pars.check_load import check_load


class LoadMaster:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def click_master_label(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'астерская')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def load_master(self):
        res_click = self.click_master_label()

        if not res_click:
            return False

        res_load = check_load(self.driver, '//*[contains(text(), "Каталог запчастей")]')

        return res_load
