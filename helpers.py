def check_index(index, length):
    """работает с индексом, чтобы он находился в пределах от 0 до length-1."""
    if index >= length:
        index -= length
    elif index < 0:
        index += length
    return index
#без этой функции и проверки в определенных словах и буквах возникает out of range

def readit(file_path, line_number):
    """Чтение строки. Превращение в список символов."""

    file = open(file_path, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    if line_number < 1 or line_number > 5:
        raise ValueError(f"Некорректная настройка Энигмы")

    selected_line = lines[line_number - 1].strip()
    code_alphabet = list(selected_line)
    code_alphabet.append(' ')  # добавляем пробел в список символов
    return code_alphabet


def check_proper_len(alphabet):
    """ Проверяет, что в алфавите ровно 34 символа """
    if len(alphabet) != 34:
        raise ValueError("неверная конфигурация. Проверьте настройку ротора и рефлектора")
#проверяет роторы (где вместе с пробелом 34 символа будет)
#проверят рефлекторы (после обработки там тоже будет список из 34 символов)


def check_initial_let(start_p):
    """ Проверяет, что задано 3 символа """
    if len(start_p) != 3:
        raise ValueError("Ошибка. Введите 3 символа.")


def changes_dictionary(file_path, line_number):
    """Создает словарь соответствий из строки файла.
    Из 17 пар букв сделает 34. Например, АБ превращается в А: Б, Б:А"""

    file = open(file_path, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    line = lines[line_number - 1]
    changes = line.split()# разбиваем строку на пары букв, разделенные пробелам
    swap = {}  # замены

    # обработка каждой пары
    for letters in changes:
        if len(letters) != 2: #если где-то будет например АБВ Г ДЕ...
            raise ValueError(f"неправильный формат пары: {letters}")

        first, second = letters[0], letters[1]

        # как написано в readme файле: пробел -- нижнее подчеркивание
        if first == '_':
            first = ' '
        if second == '_':
            second = ' '

        swap[first] = second
        swap[second] = first

    return swap


#reflections = changes_dictionary('settings.txt', 5)
#print(reflections)
