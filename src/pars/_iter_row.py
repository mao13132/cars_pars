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

from src.pars.get_all_rows import get_all_rows
from src.pars.switcher_type import SwitcherType


class IterRow:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def get_type_row(self, row):
        try:
            type = row.get_attribute('row_type')
        except:
            return False

        return type

    def _iter_row(self, count_rows):

        switcher_core = SwitcherType(self.settings)

        for row_range in range(count_rows):
            rows_list = get_all_rows(self.driver)

            target_row = rows_list[row_range]

            type_row = self.get_type_row(target_row)

            target = switcher_core.switcher(type_row, target_row)

            print(f'Итерирую строчку "{row_range}"')

    def iter_row(self, count_rows):
        res_iter = self._iter_row(count_rows)

        print()
