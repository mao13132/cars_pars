# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.browser.createbrowser_uc import CreatBrowser
from src.pars.start_pars import StartPars
import traceback
import sys


def main(browser):

    if not browser.driver:
        return False

    settings = {
        'driver': browser.driver
    }

    res_job = StartPars(settings).start_pars()

    print()


if __name__ == '__main__':

    browser = CreatBrowser()

    try:
        main(browser)
    except Exception as es:
        print(f"Ошибка при работе главного потока"
              f"{''.join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))}")

    finally:

        browser.driver.quit()
