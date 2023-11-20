import random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.iter_items = iter(items) if isinstance(items, list) else items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.duplicates = []

    def __next__(self):
        while True:
            try:
                cur = next(self.iter_items)

                if self.ignore_case:
                    cur_check = cur.lower()
                else:
                    cur_check = cur

                if cur_check not in self.duplicates:
                    self.duplicates.append(cur_check)
                    return cur_check

            except Exception:
                raise StopIteration

    def __iter__(self):
        return self


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
letters = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
data = gen_random(10, 1, 3)

print([x for x in Unique(numbers)])
print([x for x in Unique(letters)])
print([x for x in Unique(data)])
print([x for x in Unique(['A', 'a', 'B', 'b'])])
print([x for x in Unique(['A', 'a', 'B', 'b'], ignore_case=True)])