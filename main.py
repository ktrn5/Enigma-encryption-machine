#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import enigma
import user_input
import helpers


"""readme: ФОРМАТ ФАЙЛА С КОНФИГУРАЦИЕЙ: 5 строк
1 строчка: 1 ротор (конфигурация для ротора; кол-во букв должно соответствовать кол-ву букв в алфавите)
2 строчка: 2 ротор
3 строчка: 3 ротор
4 строчка: настройка панели, каждую пару букв написать через панель
5 строчка: рефлектор, необходимо написать 17 пар букв (в алфавите всего 34 с учетом пробела). 
           Например: АБ ЯН Л_ ......, где _ означает пробел. Каждая буква должна встретиться лишь 1 раз
           
сам пользователь (без файла) вводит начальные положения роторов и текст"""

def create_parser():
    """парсер аргументов из команднной строки """

    parser = argparse.ArgumentParser()
    parser.add_argument('rotors', nargs='?')
    parser.add_argument('text', nargs='?')
    return parser


def main():
    """ основная функция программы. Запуск"""
    parser = create_parser()
    namespace = parser.parse_args()

    # Если аргументы командной строки переданы, используем их
    if (namespace.rotors and namespace.text):
        start_p = namespace.rotors
        helpers.check_initial_let(start_p)
        cipher = namespace.text
    else:
        # Иначе запрашиваем ввод у пользователя
        start_p = user_input.get_text_rus("введите начальное значение роторов (три символа слитно): ")
        helpers.check_initial_let(start_p)
        cipher = user_input.get_text_rus("введите текст::")

    rotor1 = start_p[0]
    rotor2 = start_p[1]
    rotor3 = start_p[2]
    enigma_machine = enigma.Enigma(rotor1, rotor2, rotor3)

    cipher_result = enigma_machine.encrypr(cipher)
    print(f'результат::{cipher_result}')

main()


#C:\Users\user\PycharmProjects\Enigma
