# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def change_frame(driver):
    try:
        frame = driver.find_element(by=By.XPATH, value=f"//iframe[contains(@class, 'Iframe')]")

        driver.switch_to.frame(frame)
    except Exception as es:
        print(f'Ошибка переключения фрейма на popup "{es}"')

        return False

    return True


def back_frame(driver):
    try:
        driver.switch_to.default_content()
    except Exception as es:
        print(f'Переключение на стандартный фрейм - ошибка "{es}"')

        return False

    return True
