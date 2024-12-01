#A module related to processing user input.
#Universal functions for checking the input of numbers and text.
def get_text_rus(info):
    """Similar function to analyze text and define errors
    Using set this fuction ensure that given answer is in english"""
    letters = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    while True:
        answer = input(info).strip().upper()
        if any(char in letters for char in answer):
            return answer
        else:
            print("Ошибка! Введите текст на русском")

def get_integer(info):
    """Function: Input of the number, which is > 0.
    Use this function to get info from user (in main) + to define errors """
    while True:
        value = input(info)
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Error! Enter a NUMBER ")


def get_text_eng(info):
    """Similar function to analyze text and define errors
    Using set this fuction ensure that given answer is in english"""
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while True:
        answer = input(info).strip()
        if any(char in letters for char in answer):
            return answer
        else:
            print("Error! Enter text in English")
