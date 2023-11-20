import functools
def print_result_helper(func, res):
    print(func.__name__)
    if isinstance(res, list):
        for i in res:
            print(i)
    elif isinstance(res, dict):
        for k, v in res.items():
            print(f'{k} = {v}')
    else:
        print(res)


def print_result(func):
    @functools.wraps(func)
    def decorated_func(*args, **kwargs):
        res = func(*args, **kwargs)
        print_result_helper(func, res)
        return res
    return decorated_func
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()