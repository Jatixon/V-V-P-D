import math

# Константа для количества итераций
ITERATIONS = 10


def calculate_function(choice, x):
    """
    Вычисляет значение функции (sin(x) или ln(1-x)) с помощью ряда Маклорена.

    :param choice: выбор функции (1 - sin(x), 2 - ln(1-x))
    :param x: значение переменной для вычисления
    :return: приближённое значение функции
    :raises ValueError: если выбор функции или значение x некорректны
    """
    result = 0

    if choice == 1:  # sin(x)
        for n in range(ITERATIONS):
            result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

    elif choice == 2:  # ln(1-x)
        if not (-1 < x <= 1):
            raise ValueError("Для ln(1-x) x должен быть в пределах -1 < x <= 1.")
        for n in range(1, ITERATIONS + 1):
            result += (-1) ** (n + 1) * (x ** n) / n

    else:
        raise ValueError("Неверный выбор функции. Используйте 1 для sin(x) или 2 для ln(1-x).")

    return result


def menu():
    """
    Меню для выбора функции и ввода значения x.

    Пользователь может выбрать функцию, ввести x, и получить результат,
    который вычисляется с использованием ряда Маклорена.
    """
    print("Выберите функцию:")
    print("1. sin(x) (с помощью ряда Маклорена)")
    print("2. ln(1-x) (с помощью ряда Маклорена)")

    try:
        # Запрос у пользователя выбора функции
        choice = int(input("Введите номер функции: "))

        # Запрос значения x с проверкой
        x = float(input("Введите значение x: "))

        # Вычисление результата
        result = calculate_function(choice, x)

        # Вывод результата
        if choice == 1:
            print(f"sin({x}) ≈ {result}")
        elif choice == 2:
            print(f"ln(1-{x}) ≈ {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    """
    Основной блок выполнения программы. Запускает меню.
    """
    menu()
