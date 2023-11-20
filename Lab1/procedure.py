import sys
from math import sqrt


def get_coef(index, prompt):
    coef_str = None
    if len(sys.argv) > 1:
        try:
            coef_str = float(sys.argv[index])
        except ValueError:
            print("Некорректный аргумент командной строки.")
            sys.exit()
    else:  # случай, когда sys.argv не имеет аргументов
        # Вводим с клавиатуры, проверяем на ввод чисел
        print(prompt)
        while coef_str is None:
            try:
                coef_str = float(input("Введите число: "))
            except ValueError:
                print("Некорректный ввод!")
                continue
            break
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    discriminant = b*b - 4*a*c
    if discriminant == 0.0:
        root = sqrt(-b / (2.0*a))
        result.append(root)
    elif discriminant > 0.0:
        sqd = sqrt(discriminant)
        root1 = sqrt((-b + sqd) / (2.0*a))
        root2 = sqrt((-b - sqd) / (2.0*a))
        result.append(root1)
        result.append(root2)
    return result


def main():
    a = get_coef(1, 'Коэффициент А:')
    b = get_coef(2, 'Коэффициент B:')
    c = get_coef(3, 'Коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Два корня: +/-{}'.format(roots[0]))
    elif len_roots == 2:
        print('Четыре корня: +/-{}, +/-{}'.format(roots[0], roots[1]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()