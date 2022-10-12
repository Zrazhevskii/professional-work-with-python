from decorator import decorator


def generation(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for sub in generation(value, tree_types):
                yield sub
    else:
        yield o


@decorator
def numer(function):
    nos = []
    for item in generation(function):
        nos.append(item)
    return nos


if __name__ == '__main__':
    nested_list2 = [
        [[[[[['a']]]]], 'b', 'c'],
        [[[['d', 'e']]], 'f', 'h', False],
        [1, 2, None],
    ]

    numer(nested_list2)