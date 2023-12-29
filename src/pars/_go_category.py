# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from settings import main_category, sub_cat
from src.pars._load_category import LoadCategory


class GoCategory:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

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

        title = ''

        main_core = LoadCategory(self.settings)

        for _try in range(2):

            if _try > 0:
                target_category = sub_cat

                print(f'Проверяю под категории')

            else:
                target_category = main_category

                print(f'Получаю категории')

            main_category_list = main_core.load_category()

            if not main_category_list:
                return title

            row_category = main_category_list[target_category]

            title = self.get_title(row_category)

            res_click = self._click_category(row_category)

            time.sleep(10)

        return title
