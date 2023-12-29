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

from settings import LOGIN, PASSWORD
from src.pars.get_all_rows import get_all_rows


class WriteAuth:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def clear_input(self, target, count_):

        if not count_:
            return True

        for _try in range(count_):

            try:
                value = self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, '{target}')]") \
                    .send_keys(Keys.BACKSPACE)
            except:
                continue

        return True

    def _write_login(self):

        count_ = self.get_value('username')

        self.clear_input('username', count_)

        try:
            self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, 'username')]").send_keys(LOGIN)
        except:
            print(f'Не смог написать логин')

            return False

        return True

    def _write_password(self):

        count_ = self.get_value('password')

        self.clear_input('password', count_)

        try:
            self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, 'password')]").send_keys(PASSWORD)
        except:
            print(f'Не смог написать пароль')

            return False

        return True

    def get_value(self, target):
        try:
            value = self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, '{target}')]") \
                .get_attribute('value')
        except:

            return 0

        count_ = len(value)

        return count_

    # self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, 'username')]").send_keys(Keys.BACKSPACE)

    def start_auth(self):
        write_login = self._write_login()

        if not write_login:
            return False

        time.sleep(2)

        write_password = self._write_password()

        if not write_password:
            return False

        time.sleep(2)

        return True
