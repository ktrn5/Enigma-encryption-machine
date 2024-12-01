import helpers

file_path = 'settings.txt'
alphabet = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

class Panel:
    """Класс панель. Реализует смену букв одну на другую из заданной настройки.
    Если в настройках буквы нет, то оставляет ту, которая подана."""

    def __init__(self, change):
        self.change = change

    def panelling(self, letter):
        if letter in self.change:
            return self.change[letter]
        else:
            return letter


class Reflector:
    """Класс рефлектор. Реализует смену букв одну на другую из заданной настройки.
     Симметричная замена: обязательна четность алфавита"""

    def __init__(self, reflection):
        self.reflection = reflection
        helpers.check_proper_len(self.reflection) #проверка на то, что должно быть 17 замен (т.е. 34 пары (А:Б, Б:А и т.д...)

    def reflect(self, letter):
        return self.reflection[letter]


class Rotor:
    """Класс, обеспечивающий работу ротора"""

    def __init__(self, letter, line_number):
        """Инициализация ротора.
        letter -- начальное значение ротора
        line_number -- номер строки настроек (setting.txt), в которой заданоа конфигурация для конкретного ротора.
        1 ротор -- 1 строка, 2 - 2.... """

        self.letter = 0
        self.previous = 0
        self.alphabet = alphabet # русский алфавит + пробел
        self.code_alphabet = helpers.readit(file_path, line_number) # читаем настройку ротора с помощью моего модуля
        self.set_letter(letter)

        #проверка длины: обязательно должно быть задано в настройке 34 символа!
        helpers.check_proper_len(self.code_alphabet)
        #print(f"ключ ротора : {letter}, настройка ротора: {self.code_alphabet}")


    def encrypt(self, letter):
        """Метод для шифрования буквы "слева направо"
        (применяется в начале после панели, проходя последовательно 1,2 и 3 роторы) """

        letter = letter.upper()
        letter = self.alphabet.index(letter)
        letter = letter + (self.letter - self.previous) #сдвиг
        letter = helpers.check_index(letter, 34) #чтобы не было ошибки out of range
        return self.code_alphabet[letter] #возваращем символ на этом индексе, но уже из алфавита из конфигурации


    def reverse_encrypt(self, letter):
        """Метод для шифрования буква "справо налево"
        (применяется уже после рефлектора, проходя 3, 2 и 1 роторы"""

        letter = letter.upper()
        letter = self.code_alphabet.index(letter)
        letter = letter - (self.letter - self.previous) #сдвиг 
        letter = helpers.check_index(letter, 34) #чтобы не было ошибки out of range
        return self.alphabet[letter]


    def set_letter(self, letter):
        """Установка нач положения"""
        self.letter = self.alphabet.index(letter.upper())



