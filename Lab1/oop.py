import sys
from math import sqrt

class BiquadraticEquation:

    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.num_roots = 0  # Количество корней
        self.roots_list = []  # Список корней

    @staticmethod
    def get_coef(index, prompt):
        coef_str = None
        if len(sys.argv) > 1:
            try:
                coef_str = float(sys.argv[index])
            except ValueError:
                print("Некорректный аргумент командной строки.")
                sys.exit()
        else:  # случай, когда sys.argv не имеет аргументов
            print(prompt)
            while coef_str is None:
                try:
                    coef_str = float(input("Введите число: "))
                except ValueError:
                    print("Некорректный ввод!")
                    continue
                break
        coef = float(coef_str)
        return coef

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        discriminant = b * b - 4 * a * c
        if discriminant == 0.0:
            root = sqrt(-b / (2.0 * a))
            self.num_roots = 1
            self.roots_list.append(root)
        elif discriminant > 0.0:
            sqd = sqrt(discriminant)
            root1 = sqrt((-b + sqd) / (2.0 * a))
            root2 = sqrt((-b - sqd) / (2.0 * a))
            self.num_roots = 2
            self.roots_list.append(root1)
            self.roots_list.append(root2)

    def print_roots(self):
        # Проверка отсутствия ошибок при вычислении корней
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +
                   'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 1:
                print('Два корня: +/-{}'.format(self.roots_list[0]))
            elif self.num_roots == 2:
                print('Четыре корня: +/-{}, +/-{}'.format(self.roots_list[0], self.roots_list[1]))


def main():
    biquad = BiquadraticEquation()
    biquad.get_coefs()
    biquad.calculate_roots()
    biquad.print_roots()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()