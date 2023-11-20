import json
import sys
from lab_python_fp.cm_timer import timer
from lab_python_fp.print_result import print_result
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique as unique

path = sys.argv[1]

with open(path, encoding="utf8") as f:
    data = json.load(f)

# print(data)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


# @print_result
def f1(arg):
    return sorted([st for st in unique(field(arg, 'job-name'), ignore_case=True)], key=lambda x: x.upper())


# @print_result
def f2(arg):
    return list(filter(lambda x: x.upper().startswith('ПРОГРАММИСТ'), arg))


# @print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(len(arg), 100000, 200000)
    return [i + ', зарплата ' + str(j) + ' руб.' for i, j in zip(arg, salary)]

with timer():
    f4(f3(f2(f1(data))))