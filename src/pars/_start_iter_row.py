# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------


from src.pars._iter_row import IterRow
from src.pars.get_all_rows import get_all_rows
from src.pars.load_full_row import LoadFullRow


class StartIterRow:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def start_iter(self):
        print(f'Начинаю итерировать строчки')

        count_row = LoadFullRow(self.settings).loop_load_full_rows()

        res_iter = IterRow(self.settings).iter_row(count_row)

        print()