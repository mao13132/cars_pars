import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoadPage:
    def __init__(self, settings):

        self.driver = settings['driver']

        self.url = settings['url']

        self.xpath = settings['xpath']

    def load_page(self, ):
        try:
            self.driver.get(self.url)
            return True
        except:
            return False

    def __check_load_page(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.xpath)))
            return True
        except:
            return False

    def loop_load_page(self):
        count = 0
        count_ower = 10

        self.driver.set_page_load_timeout(15)

        while True:

            count += 1

            if count >= count_ower:
                print(f'Не смог открыть сайт проверьте прокси')
                return False

            start_page = self.load_page()

            if not start_page:
                time.sleep(5)
                continue

            check_page = self.__check_load_page()

            if not check_page:
                self.driver.refresh()

                continue

            self.driver.set_page_load_timeout(60)

            return True
