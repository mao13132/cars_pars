# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import os

from settings import dir_project


def create_dir(name_path, main_category, brand):
    path = f"{dir_project}\\data\\{main_category}"

    path2 = f"{dir_project}\\data\\{main_category}\\{brand}"

    path3 = f"{dir_project}\\data\\{main_category}\\{brand}\\{name_path}"

    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(path2):
        os.mkdir(path2)

    if not os.path.exists(path3):
        os.mkdir(path3)

    return True
