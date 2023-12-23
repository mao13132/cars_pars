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

from settings import alternative_


def _click_alternative(driver):
    try:
        driver.find_elements(by=By.XPATH,
                             value=f"//*[contains(text(), '{alternative_}')]")[0].click()
    except:

        return False

    return True


def click_alternative(driver):
    for _try in range(10):

        res_ = _click_alternative(driver)

        if not res_:
            time.sleep(1)

            continue

        return True

    print(f'Не смог кликнуть на альтернативные детали в окне')

    return False
