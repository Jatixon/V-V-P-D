Описание проекта

Этот проект предоставляет функции для вычисления значений sin⁡(x)sin(x) и ln⁡(1−x)ln(1−x) с использованием разложения в ряд Маклорена (частный случай ряда Тейлора, разложенного при x=0x=0). Программа позволяет вычислить приближённые значения этих функций для заданного значения xx, используя фиксированное количество итераций.
Функции

    calculate_function(choice, x):
    Основная функция для вычисления значений.
        Если choice = 1, вычисляется sin⁡(x)sin(x) с использованием ряда Маклорена.
        Если choice = 2, вычисляется ln⁡(1−x)ln(1−x) с использованием ряда Маклорена.

Установка

    Убедитесь, что у вас установлен Python (рекомендуемая версия 3.7 или выше).
    Скачайте файл программы на ваш компьютер.

Запуск программы

    Запустите программу с помощью команды:

    python main.py

    Следуйте инструкциям в консоли для ввода данных.

Использование

    При запуске программы вы увидите меню с выбором функций:
        1: Вычисление sin⁡(x)sin(x).
        2: Вычисление ln⁡(1−x)ln(1−x).
    Введите номер функции.
    Введите значение xx (с проверкой граничных значений для ln⁡(1−x)ln(1−x)).
    Получите результат, вычисленный с использованием фиксированного количества итераций (по умолчанию 10).

Чек-лист

    Убедитесь, что Python установлен.
    Скачайте файл main.py.
    Запустите программу.
    Выберите нужную функцию и введите значение xx.
    Проверьте результат.

Примеры кода
Пример 1: Вычисление sin⁡(x)sin(x)

import math

def sin_maclaurin(x, terms=10):
    result = 0
    for n in range(terms):
        result += (-1)**n * (x**(2*n + 1)) / math.factorial(2*n + 1)
    return result

# Пример использования
x = 1.0
result = sin_maclaurin(x)
print(f"sin({x}) ≈ {result}")

Пример 2: Вычисление ln⁡(1−x)ln(1−x)

def ln1x_maclaurin(x, terms=10):
    if not (-1 < x <= 1):
        raise ValueError("Для ln(1-x) x должен быть в пределах -1 < x <= 1.")
    result = 0
    for n in range(1, terms + 1):
        result += (-1)**(n + 1) * (x**n) / n
    return result

# Пример использования
x = 0.5
result = ln1x_maclaurin(x)
print(f"ln(1-{x}) ≈ {result}")

