# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.pars.load_page import LoadPage


class StartSite:
    def __init__(self, settings):
        self.settings = settings

    def site_inter_cars(self):
        self.settings['url'] = 'https://lv.e-cat.intercars.eu'

        self.settings['xpath'] = '//*[contains(@class, "categorynavigation__list")]'

        res_open = LoadPage(self.settings).load_page()

        time.sleep(10)

        return res_open

    def site_car_parts(self):
        self.settings['url'] = 'https://web8.carparts-cat.com/?11=478'

        self.settings['xpath'] = '//*[contains(text(), "Добро пожаловать")]'

        res_open = LoadPage(self.settings).load_page()

        time.sleep(10)

        return res_open

    def load_site(self):
        # res_open = self.site_inter_cars()
        res_open = self.site_car_parts()

        return res_open
