# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from settings import target_language, main_category
from src.pars._click_sing_in import ClickSingIn
from src.pars._go_category import GoCategory
from src.pars._start_iter_row import StartIterRow
from src.pars._load_category import LoadCategory
from src.pars._load_master import LoadMaster
from src.pars._start_site import StartSite
from src.pars.change_language import ChangeLanguage


class StartPars:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def start_pars(self):
        res_open = StartSite(self.settings).load_site()

        if not res_open:
            return False

        click_sing_in = ClickSingIn(self.settings).click_sing_in()

        if not click_sing_in:
            print(f'Не смог нажать на sign in')
            return False

        load_master = LoadMaster(self.settings).load_master()

        if not load_master:
            print(f'Не смог загрузить мастерскую')
            return False

        main_category_list = LoadCategory(self.settings).load_category()

        if not main_category_list:
            print(f'Не могу получить все категории')
            return False

        self.settings['main_category_list'] = main_category_list

        self.settings['pars_data'] = {}

        title = GoCategory(self.settings).go_category()

        if not title:
            print(f'Не мог зайти в категорию')
            return False

        self.settings['pars_data'][main_category] = {}

        self.settings['pars_data'][main_category]['title'] = title

        self.settings['pars_data'][main_category]['subcategory'] = {}

        change_language = ChangeLanguage(self.settings).change(target_language)

        if not change_language:
            return False

        res_iter = StartIterRow(self.settings).start_iter()

        print()
