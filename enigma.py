import helpers
import parts_enigma

file_path = 'settings.txt'
reflections = helpers.changes_dictionary(file_path, 5) #считываем словарь отражений
panel_changes = helpers.changes_dictionary(file_path, 4) #считываем словарь замен букв


class Enigma:
    """ Класс Enigma -- машина энигма, которая шифрует с помощью рефлектора, панели и роторов.
        Используются классы и функции из helpers и parts_enigma """

    def __init__(self, start_p1, start_p2, start_p3):
        """Инициализация класса.
         starter point = start_p. Начальные значения для роторов (вводятся пользователем в main)"""

        #рассматриваем случай, когда одним из значений может быть пробел (алфавит из 34 символом: 33 буквы и пробел)
        if (start_p1 == ''):
            start_p1 = ' '
        if (start_p2 == ''):
            start_p2 = ' '
        if (start_p3 == ''):
            start_p3 = ' '

        #инициализируем роторы с верными начальными точками + указываем строку из конфигурации (settings.txt)
        self.rotor1 = parts_enigma.Rotor(start_p1, 1)
        self.rotor2 = parts_enigma.Rotor(start_p2, 2)
        self.rotor3 = parts_enigma.Rotor(start_p3, 3)
        self.rotor1.set_letter(start_p1)
        self.rotor2.set_letter(start_p2)
        self.rotor3.set_letter(start_p3)

        #предыдущий ключ для второго ротора ставим равным текущему ключу первого ротора и аналогично для третьегл
        #для корректной обработки при обоновлении ключей
        self.rotor2.previous_letter = self.rotor1.letter
        self.rotor3.previous_letter = self.rotor2.letter

        #панель и рефлеткор
        self.panels = parts_enigma.Panel(panel_changes)  #
        self.reflector = parts_enigma.Reflector(reflections)  #


    def update(self):
        """Обновление ключей роторов.
        После полного поворота одного ротора слудующий ротор смещается на 1 шаг"""

        if (self.rotor1.letter + 1 > 33):
            if (self.rotor2.letter + 1 > 33):
                if (self.rotor3.letter + 1 > 33):
                    self.rotor3.letter = self.rotor3.letter -32 #последний ротор достиг конца, сбрасываем
                else:
                    self.rotor3.letter += 1
            else:
                self.rotor2.letter += 1
        else:
            self.rotor1.letter += 1


    def encrypr(self, text):
        """шифрование текста
        панель --> ротор --> рефлектор --> ротор --> панель """

        result = ""
        #запускаем все части машины для каждой буквы

        for letter in text:

            #print(f"Original letter: {letter}")  # just for checkup
            #letter = self.panels.panelling(letter)
            #print(f"After panel: {letter}")
            #print(f"reflector result: {letter}")
            letter = self.rotor1.encrypt(letter)
            #print(f"1rotor result: {letter}")
            letter = self.rotor2.encrypt(letter)
            letter = self.rotor3.encrypt(letter)
            letter = self.reflector.reflect(letter)
            # print(f"reflector result: {letter}")
            letter = self.rotor3.reverse_encrypt(letter)
            # print(f"3 reverse rotor result: {letter}")
            letter = self.rotor2.reverse_encrypt(letter)
            # print(f"2 reverse rotor result: {letter}")
            letter = self.rotor1.reverse_encrypt(letter)
            ##print(f"1rotor result: {letter}")

            result += letter
            self.update()

        return result


    def set_letter(self, start_p1, start_p2, start_p3):
        """Установка и обновление значений"""
        self.rotor1.set_letter(start_p1)
        self.rotor2.set_letter(start_p2)
        self.rotor3.set_letter(start_p3)
        self.rotor2.previous_letter = self.rotor1.letter
        self.rotor3.previous_letter = self.rotor2.letter
