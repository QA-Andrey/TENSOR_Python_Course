# Игра "Эрудит"
# Нужно написать программу scrabble, которая помогает считать кол-во очков (points), полученное за слово (word)
# По одному очку вы получите за буквы а, в, е=ё, и, н, о, р, с, т.
# Два очка стоит д, к, л, м, п, у.
# Три балла получают за б, г, ь, а также я.
# Четыре балла стоят буквы й, ы.
# 5 очков засчитывается за ж, з, х, ц, ч.
# 6 и 7 очков не предусмотрено.
# Восемь можно получить за букву ф, ш, э, ю.
# 10 баллов стоит буква щ,
# а 15 - ъ
# Например (Ввод --> Вывод):
# курс --> 6 (к=2, у=2, р=1, с=1)


def scrabble(word):
    """
    Считаем кол-во очков, полученное за слово в соответствии с очками за каждую букву в нем.

    :param word: Входящее слово для подсчета очков.
    :return: Количество очков за слово.
    """
    my_dict = {
        1: ["а", "в", "е", "ё", "и", "н", "о", "р", "с", "т"],
        2: ["д", "к", "л", "м", "п", "у"],
        3: ["б", "г", "ь", "я"],
        4: ["й", "ы"],
        5: ["ж", "з", "х", "ц", "ч"],
        8: ["ф", "ш", "э", "ю"],
        10: ["щ"],
        15: ["ъ"]
    }
    points = 0

    for letter in word:
        for key, value in my_dict.items():
            for index, value_2 in enumerate(value):
                if letter in value_2:
                    points = points + key

    return points

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ["курс", 'авеинорстё', 'дклмпеу', 'бгья', 'йы', 'жзхцч', 'фшэю', 'щъ', "карабасбарабас", "околоводопроводного",
        "еженедельное", 'эхоэнцефалограф', 'человеконенавистничество', 'делопроизводительница']

test_data = [6, 10, 13, 12, 8, 25, 32, 25, 21, 26, 20, 54, 34, 36]

for i, d in enumerate(data):
    assert scrabble(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')