# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def formate_price(value: str):
    symbol_list = ['.', ',']

    _value = ''

    for x in value:
        if x.isdigit() or x in symbol_list:
            _value += x

    return _value
