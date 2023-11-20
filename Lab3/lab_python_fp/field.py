goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
def field(items,*args):
    assert len(args) > 0
    for item in items:
        if len(args)==1:
            yield get_data (item, args[0])
        else:
            yield {key:get_data(item, key) for key in args}


def get_data(item, key):
    return item.get(key)

print([x for x in field(goods, 'title')])
print([x for x in field(goods, 'title', 'price')])