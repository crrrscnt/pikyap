data = [4, -30, 100, -100, 123, 1, 0, -1, -4, 30]

if __name__ == '__main__':
    # Без лямбда-функции
    print(sorted(data, key = abs, reverse=True))
    # С лямбда-функцией
    print(sorted(data, key=lambda x: abs(x), reverse=True))