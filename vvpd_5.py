import math

# Константа для количества итераций
iterations = 10


def calculate_sin(x):
    """
    Вычисляет значение функции sin(x) или ln(1-x) с помощью ряда Маклорена.

    :param choice: выбор функции (1 - sin(x), 2 - ln(1-x))
    :param x: значение переменной для вычисления
    :return: приближённое значение функции
    :raises ValueError: если выбор функции или значение x некорректны
    """
    result = 0
    for n in range(iterations):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

def calculate_ln(x):
    """
    Вычисляет значение функции ln(1-x) с помощью ряда Маклорена.

    :param x: значение переменной для вычисления
    :return: приближённое значение функции
    """
    result = 0
    for n in range(1, iterations + 1):
        result += (-1) ** (n + 1) * (x ** n) / n
    return result

def calculate_taylor(x,m):
    """
    Аппроксимация функции (1 + x)^m с использованием ряда Маклорена.

    Подробное описание:
    Ряд Маклорена для функции (1 + x)^m определяется как:
        (1 + x)^m = 1 + m*x + m*(m-1)*x^2/2! + m*(m-1)*(m-2)*x^3/3! + ...
    Функция вычисляет приближение, используя конечное количество членов ряда.

    Аргументы:
    m (float): Степень, к которой возводится выражение (1 + x).
    x (float): Входное значение для аппроксимации, -1 < x < 1.
    iterations: Количество членов в ряде для приближения.

    Возвращаемое значение:
    float: Аппроксимированное значение (1 + x)^m.

    Исключения:
    ValueError: Возникает, если 'terms' не является положительным целым числом или x не в пределах (-1, 1).

    Примеры:
    one_plus_x(2, 0.5, terms=5)
    2.25
    one_plus_x(-0.5, 0.1, terms=5)
    0.97496875

    """
    result = 0
    for n in range(iterations):
    # Вычисляем биномиальный коэффициент
        binomial_coeff = 1
        for k in range(n):
            binomial_coeff *= (m - k)
        binomial_coeff /= math.factorial(n)    
        # Добавляем текущий член ряда
        terms = binomial_coeff * (x**n)
        result += terms
    return result


def menu():
    """
    Меню для выбора функции и ввода значения x.

    Пользователь может выбрать функцию, ввести x, и получить результат,
    который вычисляется с использованием ряда Маклорена.
    """
    while True:
        print("Выберите функцию:")
        print("1. sin(x) (с помощью ряда Маклорена)")
        print("2. ln(1-x) (с помощью ряда Маклорена)")
        print("3. (1 + x)^m (Ряд Тейлора)")
        print("4. Выход")
        # Запрос у пользователя выбора функции
        choice = input("Введите номер функции: ")
        # Вывод результата
        if choice not in {'1', '2', '3', '4'}:
            print("Неверный выбор. Попробуйте снова.")
            continue
        if choice == '1':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            result = calculate_sin(x)
            print(f"sin({x}) ≈ {result}")
        elif choice == '2':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            if not (-1 < x <= 1):
                print("Для ln(1-x) x должен быть в пределах -1 < x <= 1.")
                continue
            result = calculate_ln(x)
            print(f"ln(1-{x}) ≈ {result}")
        elif choice == '3':
            try:
                x = float(input("Введите значение x: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            if not (-1 < x <= 1):
                print("Для (1 + x)^m x должен быть в пределах -1 < x <= 1.")
                continue
            try:
                m = float(input("Введите значение m: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                continue
            result = calculate_taylor(x,m)
            print(f"(1 + {x})^{m} ≈ {result}")
        elif choice == '4':
            print("Выход из программы...")
            break


if __name__ == "__main__":
    """
    Основной блок выполнения программы. Запускает меню.
    """
    menu()
