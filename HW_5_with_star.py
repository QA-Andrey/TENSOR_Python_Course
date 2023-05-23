# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    Преобразуем арабское число в римское.
    Например (Ввод --> Вывод) :
    2008 --> MMVIII

    :param val: Принимаемое арабское число.
    :return: Возвращаемое латинское число.
    """
    rev_val = (str(val))[::-1]
    my_dict = {
        "Единицы": {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'},
        "Десятки": {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'},
        "Сотни": {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'},
        "Тысячи": {1: 'M', 2: 'MM', 3: 'MMM'}
    }
    roman_str = ''

    for i, v in enumerate(rev_val):
        if int(v) > 0:
            if i == 0:
                roman_str = my_dict["Единицы"][int(v)] + roman_str
            elif i == 1:
                roman_str = my_dict["Десятки"][int(v)] + roman_str
            elif i == 2:
                roman_str = my_dict["Сотни"][int(v)] + roman_str
            elif i == 3:
                roman_str = my_dict["Тысячи"][int(v)] + roman_str

    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')