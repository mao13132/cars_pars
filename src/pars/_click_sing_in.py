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


class ClickSingIn:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def _click_sing_in(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@value,'Вход в систему')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def _click_approve(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@value,'в норме')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def click_sing_in(self):
        res_click = self._click_sing_in()

        if not res_click:
            return False

        # time.sleep(6)

        res_load = check_load(self.driver, '//*[contains(@value, "в норме")]')

        # if not res_load:
        #     return False

        click_sign_in = self._click_approve()

        if not click_sign_in:
            return False

        time.sleep(2)

        res_load = check_load(self.driver, '//*[contains(text(), "Поиск")]')

        return res_load
