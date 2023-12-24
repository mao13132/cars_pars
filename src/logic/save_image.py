# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import requests


def save_image(image, path, name_path):
    try:
        p = requests.get(image)

        out = open(path, "wb")

        out.write(p.content)

        out.close()
    except Exception as es:
        print(f'Ошибка при сохранение изображения "{name_path}" "{es}"')

        return ''

    return True
