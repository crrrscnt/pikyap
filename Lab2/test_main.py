# Тест класса Rectangle
from lab_python_oop.rectangle import *

def test_main():
    string1 = "Прямоугольник синего цвета шириной 2 и высотой 2 площадью 4."
    string2 = Rectangle("синего", 2, 2).__str__()
    assert string2 == string1