# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def get_all_rows(driver):
    try:
        rows = driver.find_elements(by=By.XPATH, value=f"//table[contains(@id, 'artikel_panel')]//tr")
    except:
        return False

    return rows
