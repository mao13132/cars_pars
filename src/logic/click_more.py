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

from settings import more_


def _click_more(driver):
    try:
        driver.find_elements(by=By.XPATH,
                             value=f"//*[contains(text(), '{more_}')]")[0].click()
    except:

        return False

    return True


def click_more(driver):
    for _try in range(3):

        res_ = _click_more(driver)

        if not res_:
            time.sleep(1)

            continue

        return True

    return False
