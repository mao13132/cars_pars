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


class ChangeLanguage:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def click_panel(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'menuPanel') and "
                                                        f"contains(@class, 'settings')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def click_panel_language(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'language_drop_down')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def click_target_language(self, language):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(),'{language}')]").click()
        except:
            return False

        time.sleep(1)

        return True

    def get_status_popup(self):
        try:
            status = self.driver.find_element(by=By.XPATH, value=f"//*[@class='settingsPanel']").get_attribute('style')
        except:
            return False

        if 'none' in status or not status:
            return False

        return True

    def loop_open_popup(self):
        for _try in range(3):
            get_status = self.get_status_popup()

            if not get_status:
                self.click_panel()

                time.sleep(1)

                continue

            return True

        print(f'Все попытки открыть окно для смены языка закончились')

        return False

    def change(self, language):
        res_click = self.loop_open_popup()

        if not res_click:
            return False

        click_language_panel = self.click_panel_language()

        click_language = self.click_target_language(language)

        no_popup = self.get_status_popup()

        time.sleep(3)

        if not no_popup:
            return True

        return False
