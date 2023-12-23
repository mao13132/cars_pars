# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def replace_symbol(value: str):
    symbol_list = ['.', ',', '-', '_', '*']

    for x in value:
        if x in symbol_list:
            value = value.replace(x, '')

    return value
