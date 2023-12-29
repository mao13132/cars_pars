import getpass
import os
import platform

import undetected_chromedriver as uc

from settings import dir_project


class CreatBrowser:

    def __init__(self):

        options = uc.ChromeOptions()
        options.add_argument("start-maximized")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('ignore-certificate-errors')
        options.add_argument("--log-level=3")

        _patch = f"{dir_project}\\src\\browser\\chromedriver.exe"

        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/120.0.0.0 Safari/537.36")

        try:
            self.driver = uc.Chrome(driver_executable_path=_patch, options=options)

        except Exception as es:
            print(f'Ошибка создания браузера {es}')

            self.driver = False
