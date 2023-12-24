# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

import requests
from selenium.webdriver.common.by import By

from settings import main_category, dir_project
from src.logic.change_frame import change_frame, back_frame
from src.logic.click_alternative import click_alternative
from src.logic.click_more import click_more
from src.logic.create_dir import create_dir
from src.logic.format_price import formate_price
from src.logic.replace_symbol import replace_symbol
from src.logic.save_image import save_image


class SwitcherType:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.target_row = self.settings['pars_data'][main_category]['subcategory']

        self.sub_category = ''

        self.brand = ''

        self.name = ''

        self.sku = ''

    def get_sub_category(self, row):
        try:
            sub_category = row.find_elements(by=By.XPATH, value=f".//td")[-1].text
        except:
            return False

        return sub_category

    def get_brand(self, row):
        try:
            brand = row.find_elements(by=By.XPATH, value=f".//td")[-1].text
        except:
            return False

        return brand

    def get_quanty(self, row):
        try:
            quanty = row.find_elements(by=By.XPATH, value=f".//tr[contains(@class, 'tr_desc_Stock')]/td")[0].text
        except:
            return False

        return quanty

    def get_sku(self, row):
        try:
            sku = row.find_element(by=By.XPATH, value=f".//*[contains(@class, 'tc_number')]"
                                                      f"//a[contains(@class, 'Art')]").text
        except:
            return False

        return sku

    def click_open_article_popup(self, row):
        try:
            sku = row.find_element(by=By.XPATH, value=f".//*[contains(@class, 'tc_number')]"
                                                      f"//a[contains(@class, 'Art')]").click()
        except:
            return False

        return sku

    def check_open(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//iframe[contains(@class, 'Iframe')]")
        except:
            return False

        return True

    def _check_open_popup_product(self):
        for _try in range(5):
            try:
                self.driver.find_element(by=By.XPATH, value=f".//*[contains(@id, 'masterpane')]"
                                                            f"//*[contains(@id, 'ad_universal') and "
                                                            f"contains(@class, 'title')]")
            except:
                time.sleep(1)

                continue

            return True

        print(f'Не могу подтвердить загрузку окно с товаром ')

        return False

    def load_popup_product(self):

        change_frame(self.driver)

        open_ = self._check_open_popup_product()

        if not open_:
            return False

        return True

    def loop_check_open(self):
        for _try in range(3):

            check = self.check_open()

            if not check:
                time.sleep(1)

                continue

            return True

        return False

    def loop_open_article_popup(self, row):

        check_open = self.check_open()

        if check_open:
            return True

        for _try in range(5):

            res_click = self.click_open_article_popup(row)

            check_open = self.loop_check_open()

            if not check_open:
                time.sleep(1)

                continue

            time.sleep(2)

            load_popup = self.load_popup_product()

            if not load_popup:
                time.sleep(1)

                continue

            return True

        print(f'Не смог открыть окно с продуктом')

        return False

    def get_price(self, row):
        try:
            price = row.find_elements(by=By.XPATH, value=f".//*[contains(@class, 'tc_price')]//tr")[0].text
        except:
            return False

        try:
            price = price.split('\n')[-1]
        except:
            return False

        price = formate_price(price)

        return price

    def get_name(self, row):
        try:
            name = row.find_elements(by=By.XPATH, value=f".//*[contains(@class, 'tr_bez')]")[-1].text
        except:
            return False

        return name

    def close_popup(self):
        for _try in range(10):

            try:
                self.driver.find_element(by=By.XPATH, value=f"//*[contains(@id, 'cboxClose')]").click()
            except:
                time.sleep(1)

                continue

            return True

        return False

    def get_image(self):
        try:
            image = self.driver.find_element(by=By.XPATH,
                                             value=f"//img[contains(@id, 'main_picture')] | "
                                                   f"//*[contains(@class, 'ad_tbl_bilder_pnl')]/img") \
                .get_attribute('src')
        except:
            return ''

        name_path = replace_symbol(self.sku)

        create_dir(name_path, main_category, self.brand)

        path = f"{dir_project}\\data\\{main_category}\\{self.brand}\\{name_path}\\logo.jpg"

        res_save = save_image(image, path, name_path)

        try:
            # image_preview = self.driver.find_elements(by=By.XPATH,
            #                                           value=f"//img[contains(@class, 'adimg_preview')]")[
            #     -1].get_attribute('src')
            image_preview = self.driver.find_elements(by=By.XPATH,
                                                      value=f"//img[contains(@class, 'adimg_preview')]")

            for count, count_image in enumerate(image_preview):
                _image = count_image.get_attribute('src')

                path_prev = f"{dir_project}\\data\\{main_category}\\{self.brand}\\{name_path}\\logo{count}.jpg"

                res_save = save_image(_image, path_prev, name_path)

                path = f'{path} | {path_prev}'

        except:
            path_prev = ''

        return path

    def _get_kriteri(self):
        try:
            value = self.driver.find_elements(by=By.XPATH,
                                              value=f"//*[contains(@id, 'kriterien')]//td[contains(@class, 'ad_td')]")
        except Exception as es:
            print(f'Ошибка получения критериев "{es}"')

            return False

        return value

    def iter_kriter(self, kriterii):

        result_dict = {}

        key = ''

        value = ''

        for count, kri_row in enumerate(kriterii):
            if count % 2 == 0:
                key = kri_row.text

                result_dict[key] = ''

            if count % 2 != 0 and count != 0:
                value = kri_row.text

                result_dict[key] = value

        return result_dict

    def get_kriteri(self):
        kriterii = self._get_kriteri()

        result_kriterii = self.iter_kriter(kriterii)

        return result_kriterii

    def get_alternative(self):
        try:
            alternative = self.driver.find_elements(by=By.XPATH, value=f"//a[contains(@class, 'Art')]")
        except Exception as es:
            print(f'Ошибка при сборе альтернатив "{es}"')

            return False

        return alternative

    def get_more(self):
        try:
            more_text = self.driver.find_element(by=By.XPATH, value=f"//table[contains(@class, "
                                                                    f"'artInf_tbl_subtb')]").text
        except:

            return ''

        return more_text

    def loop_get_alternative(self):
        res_ = click_alternative(self.driver)

        if not res_:
            return []

        time.sleep(2)

        alternative_list = self.get_alternative()

        alternative_article = [x.text for x in alternative_list]

        return alternative_article

    def loop_get_more_info(self):
        res_ = click_more(self.driver)

        if not res_:
            return ''

        time.sleep(2)

        more_text = self.get_more()

        return more_text

    def switcher(self, type_row, row):
        if not type_row:
            return False

        if type_row == 'genart':

            self.sub_category = self.get_sub_category(row)

            exists = self.target_row.get(self.sub_category, False)

            if not exists:
                self.target_row[self.sub_category] = {}

        elif type_row == 'einspeiser':

            self.brand = self.get_brand(row)

            exists = self.target_row[self.sub_category].get(self.brand, False)

            if not exists:
                self.target_row[self.sub_category][self.brand] = {}

        elif type_row == 'artikel1':
            self.sku = self.get_sku(row)

            exists = self.target_row[self.sub_category][self.brand].get(self.sku, False)

            if not exists:
                self.target_row[self.sub_category][self.brand][self.sku] = {}

            quantity = self.get_quanty(row)

            self.target_row[self.sub_category][self.brand][self.sku]['quantity'] = quantity

            price = self.get_price(row)

            self.target_row[self.sub_category][self.brand][self.sku]['price'] = price

            open_popup = self.loop_open_article_popup(row)

            if not open_popup:
                return False

            image = self.get_image()

            self.target_row[self.sub_category][self.brand][self.sku]['image'] = image

            kriterii = self.get_kriteri()

            self.target_row[self.sub_category][self.brand][self.sku]['kriterii'] = kriterii

            alternative = self.loop_get_alternative()

            self.target_row[self.sub_category][self.brand][self.sku][
                'alternative'] = alternative

            more_info = self.loop_get_more_info()

            self.target_row[self.sub_category][self.brand][self.sku]['more'] = more_info

            back_frame(self.driver)

            self.close_popup()

            print(f'Сбор доп информации')

        elif type_row == 'artikel2':

            self.name = self.get_name(row)

            self.target_row[self.sub_category][self.brand][self.sku]['name'] = self.name

        else:
            print(f'Тип не определён')

        print(f'Обработал "{self.name}"')

        return True
