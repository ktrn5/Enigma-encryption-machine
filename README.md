# Enigma-encryption-machine
World War II Enigma encryption machine for transmitting encrypted messages
============================================================

Машина состоит из:

· клавиатуры, на которой вводится текст подлежащий шифровке или расшифровке (русский алфавит)

· соединительной панели [Соединительная панель меняет местами любые 2 буквы используя специальные провода и соединители: при задании параметра панели БВ: В меняется на Б, Б меняется на В]

· роторов [осуществляют циклическую замену букв, шифрует слово: сначала прямое шифрование (слева направо) роторы 1,2,3; после рефлектора справо налево роторы 3,2,1]

· рефлектора [выполняет функцию отражения сигнала]

· набора лампочек [в Энигме при нажатии буквы подсвечивается та, на которую зашифровали]



Роторы при нажатии каждой буквы поворачиваются. После полного поворота 1 ротора 2 ротор смещается на 1 шаг. (например с 3 роторами: 1 ротор -- секундная стрелка, 2 ротор -- минутная стрелка, 3 ротор -- часовая стрелка).


============================================================

ФОРМАТ ФАЙЛА С КОНФИГУРАЦИЕЙ: 5 строк

1 строчка: 1 ротор (конфигурация для ротора; кол-во букв должно соответствовать кол-ву букв в алфавите)

2 строчка: 2 ротор

3 строчка: 3 ротор

4 строчка: настройка панели, каждую пару букв написать через панель

5 строчка: рефлектор, необходимо написать 17 пар букв (в алфавите всего 34 с учетом пробела). Например: АБ ЯН Л_ ......, где _ означает пробел. Каждая буква должна встретиться лишь 1 раз
